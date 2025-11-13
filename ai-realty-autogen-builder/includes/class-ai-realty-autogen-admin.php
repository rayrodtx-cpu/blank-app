<?php
/**
 * The admin-specific functionality of the plugin.
 */
class AI_Realty_Autogen_Admin {

    private $plugin_name;
    private $version;

    public function __construct($plugin_name, $version) {
        $this->plugin_name = $plugin_name;
        $this->version = $version;
    }

    /**
     * Register the stylesheets for the admin area.
     */
    public function enqueue_styles() {
        wp_enqueue_style(
            $this->plugin_name,
            AI_REALTY_AUTOGEN_PLUGIN_URL . 'assets/css/ai-realty-autogen-admin.css',
            array(),
            $this->version,
            'all'
        );
    }

    /**
     * Register the JavaScript for the admin area.
     */
    public function enqueue_scripts() {
        wp_enqueue_script(
            $this->plugin_name,
            AI_REALTY_AUTOGEN_PLUGIN_URL . 'assets/js/ai-realty-autogen-admin.js',
            array('jquery'),
            $this->version,
            false
        );

        // Localize script for AJAX
        wp_localize_script(
            $this->plugin_name,
            'aiRealtyAutogen',
            array(
                'ajax_url' => admin_url('admin-ajax.php'),
                'nonce' => wp_create_nonce('ai-realty-autogen-nonce'),
                'rest_url' => rest_url('ai-builder/v1/'),
                'rest_nonce' => wp_create_nonce('wp_rest')
            )
        );
    }

    /**
     * Add admin menu pages.
     */
    public function add_plugin_admin_menu() {
        // Main menu page
        add_menu_page(
            'AI Realty Autogen',
            'AI Realty',
            'manage_options',
            'ai-realty-autogen',
            array($this, 'display_plugin_admin_dashboard'),
            'dashicons-admin-site-alt3',
            30
        );

        // Dashboard submenu
        add_submenu_page(
            'ai-realty-autogen',
            'Dashboard',
            'Dashboard',
            'manage_options',
            'ai-realty-autogen',
            array($this, 'display_plugin_admin_dashboard')
        );

        // Settings submenu
        add_submenu_page(
            'ai-realty-autogen',
            'Settings',
            'Settings',
            'manage_options',
            'ai-realty-autogen-settings',
            array($this, 'display_plugin_admin_settings')
        );

        // Leads submenu
        add_submenu_page(
            'ai-realty-autogen',
            'Leads',
            'Leads',
            'manage_options',
            'ai-realty-autogen-leads',
            array($this, 'display_plugin_admin_leads')
        );

        // Agents submenu
        add_submenu_page(
            'ai-realty-autogen',
            'Agents',
            'Agents',
            'manage_options',
            'ai-realty-autogen-agents',
            array($this, 'display_plugin_admin_agents')
        );
    }

    /**
     * Display the main dashboard page.
     */
    public function display_plugin_admin_dashboard() {
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'templates/admin-dashboard.php';
    }

    /**
     * Display the settings page.
     */
    public function display_plugin_admin_settings() {
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'templates/admin-settings.php';
    }

    /**
     * Display the leads page.
     */
    public function display_plugin_admin_leads() {
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'templates/admin-leads.php';
    }

    /**
     * Display the agents page.
     */
    public function display_plugin_admin_agents() {
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'templates/admin-agents.php';
    }

    /**
     * Register plugin settings.
     */
    public function register_settings() {
        // General Settings Section
        add_settings_section(
            'ai_realty_general_section',
            'General Settings',
            array($this, 'general_section_callback'),
            'ai-realty-autogen-settings'
        );

        // API Keys Section
        add_settings_section(
            'ai_realty_api_section',
            'API Integrations',
            array($this, 'api_section_callback'),
            'ai-realty-autogen-settings'
        );

        // Register settings
        $settings = array(
            'ai_realty_claude_api_key',
            'ai_realty_ihomefinder_key',
            'ai_realty_ghl_api_key',
            'ai_realty_ghl_location_id',
            'ai_realty_auto_build_enabled',
            'ai_realty_default_city',
            'ai_realty_default_state',
            'ai_realty_site_prompt',
            'ai_realty_unsplash_api_key',
            'ai_realty_agent_cookie_name',
            'ai_realty_agent_cookie_expiry'
        );

        foreach ($settings as $setting) {
            register_setting('ai_realty_autogen_options', $setting, array(
                'sanitize_callback' => array($this, 'sanitize_settings')
            ));
        }

        // Add fields
        add_settings_field(
            'ai_realty_default_city',
            'Default City',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_general_section',
            array('field' => 'ai_realty_default_city', 'placeholder' => 'Austin')
        );

        add_settings_field(
            'ai_realty_default_state',
            'Default State',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_general_section',
            array('field' => 'ai_realty_default_state', 'placeholder' => 'TX')
        );

        add_settings_field(
            'ai_realty_claude_api_key',
            'Claude API Key (Optional)',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_api_section',
            array('field' => 'ai_realty_claude_api_key', 'type' => 'password')
        );

        add_settings_field(
            'ai_realty_ihomefinder_key',
            'iHomeFinder API Key',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_api_section',
            array('field' => 'ai_realty_ihomefinder_key', 'type' => 'password')
        );

        add_settings_field(
            'ai_realty_ghl_api_key',
            'GoHighLevel API Key',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_api_section',
            array('field' => 'ai_realty_ghl_api_key', 'type' => 'password')
        );

        add_settings_field(
            'ai_realty_ghl_location_id',
            'GoHighLevel Location ID',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_api_section',
            array('field' => 'ai_realty_ghl_location_id')
        );

        add_settings_field(
            'ai_realty_unsplash_api_key',
            'Unsplash API Key',
            array($this, 'text_field_callback'),
            'ai-realty-autogen-settings',
            'ai_realty_api_section',
            array('field' => 'ai_realty_unsplash_api_key', 'type' => 'password')
        );
    }

    public function general_section_callback() {
        echo '<p>Configure the default settings for your real estate website.</p>';
    }

    public function api_section_callback() {
        echo '<p>Enter your API keys for various integrations. All keys are securely stored.</p>';
    }

    public function text_field_callback($args) {
        $field = $args['field'];
        $type = isset($args['type']) ? $args['type'] : 'text';
        $placeholder = isset($args['placeholder']) ? $args['placeholder'] : '';
        $value = get_option($field, '');

        echo '<input type="' . esc_attr($type) . '" name="' . esc_attr($field) . '" value="' . esc_attr($value) . '" placeholder="' . esc_attr($placeholder) . '" class="regular-text" />';
    }

    public function sanitize_settings($input) {
        return sanitize_text_field($input);
    }
}
