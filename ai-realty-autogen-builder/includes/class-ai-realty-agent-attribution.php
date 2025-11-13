<?php
/**
 * Agent Attribution Cookie System
 * Tracks agent IDs via cookies and attaches them to lead forms.
 */
class AI_Realty_Agent_Attribution {

    private $cookie_name;
    private $cookie_expiry;

    public function __construct() {
        $this->cookie_name = get_option('ai_realty_agent_cookie_name', 'agent_ref');
        $this->cookie_expiry = get_option('ai_realty_agent_cookie_expiry', 30) * DAY_IN_SECONDS;
    }

    /**
     * Set agent cookie from URL parameter.
     * Listens for ?agent=### in the URL.
     */
    public function set_agent_cookie() {
        if (isset($_GET['agent']) && !empty($_GET['agent'])) {
            $agent_id = sanitize_text_field($_GET['agent']);

            // Validate agent exists
            if ($this->agent_exists($agent_id)) {
                setcookie(
                    $this->cookie_name,
                    $agent_id,
                    time() + $this->cookie_expiry,
                    COOKIEPATH,
                    COOKIE_DOMAIN,
                    is_ssl(),
                    true // httponly
                );

                $_COOKIE[$this->cookie_name] = $agent_id;

                error_log("Agent cookie set: {$agent_id}");
            }
        }
    }

    /**
     * Get the current agent ID from cookie.
     */
    public function get_agent_id() {
        if (isset($_COOKIE[$this->cookie_name])) {
            return sanitize_text_field($_COOKIE[$this->cookie_name]);
        }
        return '';
    }

    /**
     * Add agent ID to Contact Form 7 hidden fields.
     */
    public function add_agent_to_cf7($fields) {
        $agent_id = $this->get_agent_id();

        if (!empty($agent_id)) {
            $fields['agent-id'] = $agent_id;
        }

        return $fields;
    }

    /**
     * Check if agent exists in database.
     */
    private function agent_exists($agent_id) {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_agents';

        $exists = $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM $table WHERE agent_id = %s",
            $agent_id
        ));

        return $exists > 0;
    }

    /**
     * Save lead to database.
     */
    public function save_lead($data) {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_leads';

        $lead_data = array(
            'name' => sanitize_text_field($data['name']),
            'email' => sanitize_email($data['email']),
            'phone' => sanitize_text_field($data['phone'] ?? ''),
            'message' => sanitize_textarea_field($data['message'] ?? ''),
            'agent_id' => $this->get_agent_id(),
            'source' => sanitize_text_field($data['source'] ?? 'contact_form'),
            'ghl_synced' => 0,
            'created_at' => current_time('mysql')
        );

        $result = $wpdb->insert($table, $lead_data);

        if ($result) {
            // Attempt to sync with GoHighLevel if configured
            $ghl_integration = new AI_Realty_GoHighLevel_Integration();
            if ($ghl_integration->is_configured()) {
                $ghl_integration->sync_lead($wpdb->insert_id);
            }

            return $wpdb->insert_id;
        }

        return false;
    }

    /**
     * Get leads for a specific agent.
     */
    public function get_agent_leads($agent_id, $limit = 50) {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_leads';

        return $wpdb->get_results($wpdb->prepare(
            "SELECT * FROM $table WHERE agent_id = %s ORDER BY created_at DESC LIMIT %d",
            $agent_id,
            $limit
        ));
    }

    /**
     * Get all leads.
     */
    public function get_all_leads($limit = 100, $offset = 0) {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_leads';

        return $wpdb->get_results($wpdb->prepare(
            "SELECT * FROM $table ORDER BY created_at DESC LIMIT %d OFFSET %d",
            $limit,
            $offset
        ));
    }

    /**
     * Get leads count.
     */
    public function get_leads_count() {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_leads';

        return $wpdb->get_var("SELECT COUNT(*) FROM $table");
    }
}
