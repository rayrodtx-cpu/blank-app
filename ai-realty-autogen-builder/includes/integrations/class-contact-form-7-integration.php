<?php
/**
 * Contact Form 7 Integration
 * Handles form submissions and lead capture.
 */
class AI_Realty_Contact_Form_7_Integration {

    public function __construct() {
        if ($this->is_active()) {
            add_action('wpcf7_before_send_mail', array($this, 'handle_form_submission'));
        }
    }

    /**
     * Check if Contact Form 7 is active.
     */
    public function is_active() {
        return is_plugin_active('contact-form-7/wp-contact-form-7.php') && class_exists('WPCF7_ContactForm');
    }

    /**
     * Handle Contact Form 7 submission.
     */
    public function handle_form_submission($contact_form) {
        $submission = WPCF7_Submission::get_instance();

        if (!$submission) {
            return;
        }

        $posted_data = $submission->get_posted_data();

        // Extract lead data
        $lead_data = array(
            'name' => $posted_data['your-name'] ?? '',
            'email' => $posted_data['your-email'] ?? '',
            'phone' => $posted_data['your-phone'] ?? '',
            'message' => $posted_data['your-message'] ?? '',
            'source' => 'contact-form-7',
        );

        // Save lead to database
        $attribution = new AI_Realty_Agent_Attribution();
        $lead_id = $attribution->save_lead($lead_data);

        if ($lead_id) {
            error_log("Contact Form 7 lead saved: ID {$lead_id}");
        }
    }

    /**
     * Create a contact form programmatically.
     */
    public function create_form($title, $form_template, $mail_template) {
        if (!$this->is_active()) {
            return false;
        }

        $contact_form = WPCF7_ContactForm::get_instance();
        $contact_form->set_title($title);
        $contact_form->set_properties(array(
            'form' => $form_template,
            'mail' => array(
                'subject' => "Contact Form: {$title}",
                'sender' => '[your-name] <[your-email]>',
                'body' => $mail_template,
                'recipient' => get_option('admin_email'),
            ),
        ));

        $result = $contact_form->save();

        if ($result) {
            return $contact_form->id();
        }

        return false;
    }

    /**
     * Get default contact form template.
     */
    public function get_default_form_template() {
        return '<label> Your Name (required)
    [text* your-name] </label>

<label> Your Email (required)
    [email* your-email] </label>

<label> Phone
    [tel your-phone] </label>

<label> Your Message
    [textarea your-message] </label>

[hidden agent-id]

[submit "Send"]';
    }

    /**
     * Get default mail template.
     */
    public function get_default_mail_template() {
        return 'From: [your-name] <[your-email]>
Subject: New Contact Form Submission

Name: [your-name]
Email: [your-email]
Phone: [your-phone]
Agent: [agent-id]

Message:
[your-message]

---
This lead was captured via the AI Realty Autogen Builder';
    }

    /**
     * Add custom validation rules.
     */
    public function add_validation_filter() {
        add_filter('wpcf7_validate_email*', array($this, 'custom_email_validation'), 20, 2);
    }

    /**
     * Custom email validation.
     */
    public function custom_email_validation($result, $tag) {
        $name = $tag->name;
        $value = isset($_POST[$name]) ? trim($_POST[$name]) : '';

        // Add custom validation logic here
        if (!empty($value) && !is_email($value)) {
            $result->invalidate($tag, 'Please enter a valid email address.');
        }

        return $result;
    }
}
