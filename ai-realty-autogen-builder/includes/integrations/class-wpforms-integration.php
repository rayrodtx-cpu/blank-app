<?php
/**
 * WPForms Lite Integration
 * Alternative form builder integration.
 */
class AI_Realty_WPForms_Integration {

    public function __construct() {
        if ($this->is_active()) {
            add_action('wpforms_process_complete', array($this, 'handle_form_submission'), 10, 4);
        }
    }

    /**
     * Check if WPForms is active.
     */
    public function is_active() {
        return (is_plugin_active('wpforms-lite/wpforms.php') || is_plugin_active('wpforms/wpforms.php'))
               && function_exists('wpforms');
    }

    /**
     * Handle WPForms submission.
     */
    public function handle_form_submission($fields, $entry, $form_data, $entry_id) {
        // Extract lead data from fields
        $lead_data = array(
            'name' => '',
            'email' => '',
            'phone' => '',
            'message' => '',
            'source' => 'wpforms',
        );

        foreach ($fields as $field_id => $field) {
            $field_type = $field['type'];
            $field_value = $field['value'];

            switch ($field_type) {
                case 'name':
                    $lead_data['name'] = $field_value;
                    break;
                case 'email':
                    $lead_data['email'] = $field_value;
                    break;
                case 'phone':
                    $lead_data['phone'] = $field_value;
                    break;
                case 'textarea':
                    $lead_data['message'] = $field_value;
                    break;
            }
        }

        // Save lead to database
        if (!empty($lead_data['email'])) {
            $attribution = new AI_Realty_Agent_Attribution();
            $lead_id = $attribution->save_lead($lead_data);

            if ($lead_id) {
                error_log("WPForms lead saved: ID {$lead_id}");
            }
        }
    }

    /**
     * Create a WPForms form programmatically.
     */
    public function create_form($title, $description = '') {
        if (!$this->is_active() || !function_exists('wpforms')) {
            return false;
        }

        $form_data = array(
            'field_id' => 4,
            'fields' => array(
                '0' => array(
                    'id' => '0',
                    'type' => 'name',
                    'label' => 'Name',
                    'required' => '1',
                    'size' => 'medium',
                ),
                '1' => array(
                    'id' => '1',
                    'type' => 'email',
                    'label' => 'Email',
                    'required' => '1',
                    'size' => 'medium',
                ),
                '2' => array(
                    'id' => '2',
                    'type' => 'phone',
                    'label' => 'Phone',
                    'format' => 'us',
                    'size' => 'medium',
                ),
                '3' => array(
                    'id' => '3',
                    'type' => 'textarea',
                    'label' => 'Message',
                    'size' => 'medium',
                ),
            ),
            'settings' => array(
                'form_title' => $title,
                'form_desc' => $description,
                'submit_text' => 'Submit',
                'notification_enable' => '1',
                'notifications' => array(
                    1 => array(
                        'email' => get_option('admin_email'),
                        'subject' => 'New Form Submission',
                        'sender_name' => get_option('blogname'),
                        'sender_address' => get_option('admin_email'),
                        'message' => '{all_fields}',
                    ),
                ),
            ),
            'meta' => array(
                'template' => 'blank',
            ),
        );

        $form_id = wpforms()->form->add(
            $title,
            $form_data,
            array(
                'template' => 'blank',
            )
        );

        if ($form_id) {
            error_log("WPForms form created: ID {$form_id}");
            return $form_id;
        }

        return false;
    }

    /**
     * Get form by title.
     */
    public function get_form_by_title($title) {
        if (!$this->is_active()) {
            return false;
        }

        $forms = wpforms()->form->get('', array(
            'orderby' => 'title',
        ));

        foreach ($forms as $form) {
            if ($form->post_title === $title) {
                return $form->ID;
            }
        }

        return false;
    }

    /**
     * Add agent ID field to form.
     */
    public function add_agent_field_to_form($form_id) {
        if (!$this->is_active()) {
            return false;
        }

        $form = wpforms()->form->get($form_id);

        if (!$form) {
            return false;
        }

        $form_data = wpforms_decode($form->post_content);

        // Add hidden agent ID field
        $form_data['fields'][] = array(
            'id' => count($form_data['fields']),
            'type' => 'hidden',
            'label' => 'Agent ID',
            'default_value' => '{agent_ref}',
        );

        // Update form
        wpforms()->form->update(
            $form_id,
            $form_data
        );

        return true;
    }
}
