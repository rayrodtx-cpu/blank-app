<?php
/**
 * Fired during plugin activation.
 */
class AI_Realty_Autogen_Activator {

    /**
     * Activation tasks.
     */
    public static function activate() {
        // Set default options
        $default_options = array(
            'ai_realty_claude_api_key' => '',
            'ai_realty_ihomefinder_key' => '',
            'ai_realty_ghl_api_key' => '',
            'ai_realty_ghl_location_id' => '',
            'ai_realty_auto_build_enabled' => false,
            'ai_realty_default_city' => 'Austin',
            'ai_realty_default_state' => 'TX',
            'ai_realty_site_prompt' => '',
            'ai_realty_installed_plugins' => array(),
            'ai_realty_build_status' => 'not_started',
            'ai_realty_unsplash_api_key' => '',
            'ai_realty_agent_cookie_name' => 'agent_ref',
            'ai_realty_agent_cookie_expiry' => 30, // days
        );

        foreach ($default_options as $option => $value) {
            if (get_option($option) === false) {
                add_option($option, $value);
            }
        }

        // Create custom tables if needed
        global $wpdb;
        $charset_collate = $wpdb->get_charset_collate();

        // Leads table
        $table_name = $wpdb->prefix . 'ai_realty_leads';
        $sql = "CREATE TABLE IF NOT EXISTS $table_name (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            name varchar(255) NOT NULL,
            email varchar(255) NOT NULL,
            phone varchar(50) DEFAULT '',
            message text DEFAULT '',
            agent_id varchar(50) DEFAULT '',
            source varchar(100) DEFAULT 'contact_form',
            ghl_synced tinyint(1) DEFAULT 0,
            created_at datetime DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY  (id),
            KEY agent_id (agent_id),
            KEY email (email)
        ) $charset_collate;";

        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);

        // Create agents table
        $agents_table = $wpdb->prefix . 'ai_realty_agents';
        $sql_agents = "CREATE TABLE IF NOT EXISTS $agents_table (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            agent_id varchar(50) NOT NULL UNIQUE,
            name varchar(255) NOT NULL,
            email varchar(255) NOT NULL,
            phone varchar(50) DEFAULT '',
            bio text DEFAULT '',
            photo_url varchar(500) DEFAULT '',
            ghl_contact_id varchar(100) DEFAULT '',
            created_at datetime DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY  (id),
            KEY agent_id (agent_id)
        ) $charset_collate;";

        dbDelta($sql_agents);

        // Flush rewrite rules
        flush_rewrite_rules();

        // Log activation
        error_log('AI Realty Autogen Builder activated successfully');
    }
}
