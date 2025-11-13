<?php
/**
 * GoHighLevel Lead Connector Integration
 * Syncs leads to GoHighLevel CRM automatically.
 */
class AI_Realty_GoHighLevel_Integration {

    private $api_key;
    private $location_id;
    private $api_url = 'https://rest.gohighlevel.com/v1';

    public function __construct() {
        $this->api_key = get_option('ai_realty_ghl_api_key', '');
        $this->location_id = get_option('ai_realty_ghl_location_id', '');
    }

    /**
     * Check if GoHighLevel is configured.
     */
    public function is_configured() {
        return !empty($this->api_key) && !empty($this->location_id);
    }

    /**
     * Sync a lead to GoHighLevel.
     */
    public function sync_lead($lead_id) {
        if (!$this->is_configured()) {
            error_log('GoHighLevel not configured. Skipping sync.');
            return false;
        }

        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_leads';

        $lead = $wpdb->get_row($wpdb->prepare(
            "SELECT * FROM $table WHERE id = %d",
            $lead_id
        ));

        if (!$lead) {
            return false;
        }

        // Check if already synced
        if ($lead->ghl_synced) {
            error_log("Lead {$lead_id} already synced to GoHighLevel.");
            return true;
        }

        // Prepare contact data
        $contact_data = array(
            'firstName' => $this->extract_first_name($lead->name),
            'lastName' => $this->extract_last_name($lead->name),
            'email' => $lead->email,
            'phone' => $lead->phone,
            'source' => $lead->source,
            'locationId' => $this->location_id,
            'tags' => array('website-lead', 'real-estate'),
        );

        // Add custom fields
        if (!empty($lead->message)) {
            $contact_data['customFields'] = array(
                array(
                    'key' => 'inquiry_message',
                    'value' => $lead->message
                )
            );
        }

        // Add agent ID if available
        if (!empty($lead->agent_id)) {
            $contact_data['tags'][] = "agent-{$lead->agent_id}";
        }

        // Make API request
        $response = $this->make_api_request('contacts', 'POST', $contact_data);

        if ($response && isset($response['contact']['id'])) {
            // Update lead as synced
            $wpdb->update(
                $table,
                array('ghl_synced' => 1),
                array('id' => $lead_id),
                array('%d'),
                array('%d')
            );

            error_log("Lead {$lead_id} synced to GoHighLevel successfully. Contact ID: {$response['contact']['id']}");
            return $response['contact']['id'];
        }

        error_log("Failed to sync lead {$lead_id} to GoHighLevel.");
        return false;
    }

    /**
     * Sync all unsynced leads.
     */
    public function sync_all_leads() {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_leads';

        $unsynced_leads = $wpdb->get_results(
            "SELECT id FROM $table WHERE ghl_synced = 0"
        );

        $synced_count = 0;
        foreach ($unsynced_leads as $lead) {
            if ($this->sync_lead($lead->id)) {
                $synced_count++;
            }
            // Rate limiting: wait 500ms between requests
            usleep(500000);
        }

        return array(
            'total' => count($unsynced_leads),
            'synced' => $synced_count
        );
    }

    /**
     * Create or update contact in GoHighLevel.
     */
    public function upsert_contact($contact_data) {
        if (!$this->is_configured()) {
            return false;
        }

        // Try to find existing contact by email
        $existing = $this->find_contact_by_email($contact_data['email']);

        if ($existing) {
            // Update existing contact
            return $this->make_api_request(
                "contacts/{$existing['id']}",
                'PUT',
                $contact_data
            );
        } else {
            // Create new contact
            $contact_data['locationId'] = $this->location_id;
            return $this->make_api_request('contacts', 'POST', $contact_data);
        }
    }

    /**
     * Find contact by email.
     */
    public function find_contact_by_email($email) {
        $response = $this->make_api_request(
            "contacts/lookup?email=" . urlencode($email),
            'GET'
        );

        if ($response && isset($response['contacts'][0])) {
            return $response['contacts'][0];
        }

        return false;
    }

    /**
     * Add note to contact.
     */
    public function add_contact_note($contact_id, $note) {
        return $this->make_api_request(
            "contacts/{$contact_id}/notes",
            'POST',
            array('body' => $note)
        );
    }

    /**
     * Add tag to contact.
     */
    public function add_contact_tag($contact_id, $tag) {
        return $this->make_api_request(
            "contacts/{$contact_id}/tags",
            'POST',
            array('tags' => array($tag))
        );
    }

    /**
     * Make API request to GoHighLevel.
     */
    private function make_api_request($endpoint, $method = 'GET', $data = null) {
        $url = $this->api_url . '/' . ltrim($endpoint, '/');

        $args = array(
            'method' => $method,
            'headers' => array(
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json',
            ),
            'timeout' => 30,
        );

        if ($data && in_array($method, array('POST', 'PUT', 'PATCH'))) {
            $args['body'] = json_encode($data);
        }

        $response = wp_remote_request($url, $args);

        if (is_wp_error($response)) {
            error_log('GoHighLevel API Error: ' . $response->get_error_message());
            return false;
        }

        $status_code = wp_remote_retrieve_response_code($response);
        $body = wp_remote_retrieve_body($response);

        if ($status_code >= 200 && $status_code < 300) {
            return json_decode($body, true);
        } else {
            error_log("GoHighLevel API Error (Status {$status_code}): {$body}");
            return false;
        }
    }

    /**
     * Extract first name from full name.
     */
    private function extract_first_name($full_name) {
        $parts = explode(' ', trim($full_name));
        return $parts[0];
    }

    /**
     * Extract last name from full name.
     */
    private function extract_last_name($full_name) {
        $parts = explode(' ', trim($full_name));
        if (count($parts) > 1) {
            array_shift($parts);
            return implode(' ', $parts);
        }
        return '';
    }

    /**
     * Test API connection.
     */
    public function test_connection() {
        if (!$this->is_configured()) {
            return array(
                'success' => false,
                'message' => 'API credentials not configured.'
            );
        }

        $response = $this->make_api_request('locations/' . $this->location_id, 'GET');

        if ($response) {
            return array(
                'success' => true,
                'message' => 'Connected to GoHighLevel successfully!',
                'location' => $response['location']['name'] ?? 'Unknown'
            );
        }

        return array(
            'success' => false,
            'message' => 'Failed to connect to GoHighLevel. Check your credentials.'
        );
    }
}
