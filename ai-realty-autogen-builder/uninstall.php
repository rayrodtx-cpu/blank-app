<?php
/**
 * Fired when the plugin is uninstalled.
 *
 * When populating this file, consider the following flow:
 * - Check if the $_REQUEST content actually is the plugin name
 * - Run an admin referrer check to make sure it's a valid request
 * - Verify the output of $_GET makes sense
 * - Repeat with other user roles. Best directly by using the links/query string parameters.
 * - Repeat things for multisite. Once for a single site in the network, once sitewide.
 */

// If uninstall not called from WordPress, then exit.
if (!defined('WP_UNINSTALL_PLUGIN')) {
    exit;
}

/**
 * Delete plugin options
 */
$options = array(
    'ai_realty_claude_api_key',
    'ai_realty_ihomefinder_key',
    'ai_realty_ghl_api_key',
    'ai_realty_ghl_location_id',
    'ai_realty_auto_build_enabled',
    'ai_realty_default_city',
    'ai_realty_default_state',
    'ai_realty_site_prompt',
    'ai_realty_installed_plugins',
    'ai_realty_build_status',
    'ai_realty_build_log',
    'ai_realty_unsplash_api_key',
    'ai_realty_agent_cookie_name',
    'ai_realty_agent_cookie_expiry',
    'ai_realty_api_key',
);

foreach ($options as $option) {
    delete_option($option);
}

/**
 * Drop custom tables
 *
 * WARNING: This will permanently delete all leads and agent data!
 * Comment out if you want to preserve data.
 */

global $wpdb;

// Drop leads table
$leads_table = $wpdb->prefix . 'ai_realty_leads';
$wpdb->query("DROP TABLE IF EXISTS {$leads_table}");

// Drop agents table
$agents_table = $wpdb->prefix . 'ai_realty_agents';
$wpdb->query("DROP TABLE IF EXISTS {$agents_table}");

/**
 * Delete property custom post type posts (if created)
 */
$properties = get_posts(array(
    'post_type' => 'property',
    'numberposts' => -1,
    'post_status' => 'any',
));

foreach ($properties as $property) {
    wp_delete_post($property->ID, true);
}

/**
 * Clean up any transients
 */
delete_transient('ai_realty_build_progress');
delete_transient('ai_realty_plugin_check');

/**
 * Log uninstall
 */
error_log('AI Realty Autogen Builder uninstalled - all data removed');
