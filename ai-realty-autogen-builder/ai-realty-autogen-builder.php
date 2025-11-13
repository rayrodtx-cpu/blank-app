<?php
/**
 * Plugin Name: AI Realty Autogen Builder
 * Plugin URI: https://github.com/yourusername/ai-realty-autogen-builder
 * Description: Autonomous AI-powered real estate website builder. Creates complete websites from natural language prompts using free WordPress tools and Claude MCP integration.
 * Version: 1.0.0
 * Author: AI Realty Dev Team
 * Author URI: https://example.com
 * License: GPL-2.0+
 * License URI: http://www.gnu.org/licenses/gpl-2.0.txt
 * Text Domain: ai-realty-autogen
 * Domain Path: /languages
 * Requires at least: 6.0
 * Requires PHP: 8.0
 */

// If this file is called directly, abort.
if (!defined('WPINC')) {
    die;
}

/**
 * Plugin version
 */
define('AI_REALTY_AUTOGEN_VERSION', '1.0.0');
define('AI_REALTY_AUTOGEN_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('AI_REALTY_AUTOGEN_PLUGIN_URL', plugin_dir_url(__FILE__));
define('AI_REALTY_AUTOGEN_PLUGIN_BASENAME', plugin_basename(__FILE__));

/**
 * The code that runs during plugin activation.
 */
function activate_ai_realty_autogen() {
    require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-autogen-activator.php';
    AI_Realty_Autogen_Activator::activate();
}

/**
 * The code that runs during plugin deactivation.
 */
function deactivate_ai_realty_autogen() {
    require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-autogen-deactivator.php';
    AI_Realty_Autogen_Deactivator::deactivate();
}

register_activation_hook(__FILE__, 'activate_ai_realty_autogen');
register_deactivation_hook(__FILE__, 'deactivate_ai_realty_autogen');

/**
 * The core plugin class
 */
require AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-autogen.php';

/**
 * Begins execution of the plugin.
 */
function run_ai_realty_autogen() {
    $plugin = new AI_Realty_Autogen();
    $plugin->run();
}
run_ai_realty_autogen();
