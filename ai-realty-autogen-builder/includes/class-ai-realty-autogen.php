<?php
/**
 * The core plugin class.
 *
 * This is used to define internationalization, admin-specific hooks, and
 * public-facing site hooks.
 */
class AI_Realty_Autogen {

    /**
     * The loader that's responsible for maintaining and registering all hooks.
     */
    protected $loader;

    /**
     * The unique identifier of this plugin.
     */
    protected $plugin_name;

    /**
     * The current version of the plugin.
     */
    protected $version;

    /**
     * Define the core functionality of the plugin.
     */
    public function __construct() {
        $this->version = AI_REALTY_AUTOGEN_VERSION;
        $this->plugin_name = 'ai-realty-autogen';

        $this->load_dependencies();
        $this->define_admin_hooks();
        $this->define_public_hooks();
        $this->define_mcp_hooks();
    }

    /**
     * Load the required dependencies for this plugin.
     */
    private function load_dependencies() {
        // Core loader
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-autogen-loader.php';

        // Admin functionality
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-autogen-admin.php';

        // Public-facing functionality
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-autogen-public.php';

        // Site builder engine
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-site-builder.php';

        // Plugin integrations
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/integrations/class-elementor-integration.php';
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/integrations/class-rankmath-integration.php';
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/integrations/class-contact-form-7-integration.php';
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/integrations/class-wpforms-integration.php';
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/integrations/class-ihomefinder-integration.php';
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/integrations/class-gohighlevel-integration.php';

        // MCP API
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'mcp/class-ai-realty-mcp-api.php';

        // Cookie attribution system
        require_once AI_REALTY_AUTOGEN_PLUGIN_DIR . 'includes/class-ai-realty-agent-attribution.php';

        $this->loader = new AI_Realty_Autogen_Loader();
    }

    /**
     * Register all of the hooks related to the admin area functionality.
     */
    private function define_admin_hooks() {
        $plugin_admin = new AI_Realty_Autogen_Admin($this->get_plugin_name(), $this->get_version());

        $this->loader->add_action('admin_enqueue_scripts', $plugin_admin, 'enqueue_styles');
        $this->loader->add_action('admin_enqueue_scripts', $plugin_admin, 'enqueue_scripts');
        $this->loader->add_action('admin_menu', $plugin_admin, 'add_plugin_admin_menu');
        $this->loader->add_action('admin_init', $plugin_admin, 'register_settings');
    }

    /**
     * Register all of the hooks related to the public-facing functionality.
     */
    private function define_public_hooks() {
        $plugin_public = new AI_Realty_Autogen_Public($this->get_plugin_name(), $this->get_version());

        $this->loader->add_action('wp_enqueue_scripts', $plugin_public, 'enqueue_styles');
        $this->loader->add_action('wp_enqueue_scripts', $plugin_public, 'enqueue_scripts');

        // Agent attribution cookie system
        $attribution = new AI_Realty_Agent_Attribution();
        $this->loader->add_action('init', $attribution, 'set_agent_cookie');
        $this->loader->add_filter('wpcf7_form_hidden_fields', $attribution, 'add_agent_to_cf7', 10, 1);
    }

    /**
     * Register all MCP REST API endpoints.
     */
    private function define_mcp_hooks() {
        $mcp_api = new AI_Realty_MCP_API();
        $this->loader->add_action('rest_api_init', $mcp_api, 'register_routes');
    }

    /**
     * Run the loader to execute all of the hooks with WordPress.
     */
    public function run() {
        $this->loader->run();
    }

    /**
     * The name of the plugin used to uniquely identify it.
     */
    public function get_plugin_name() {
        return $this->plugin_name;
    }

    /**
     * The reference to the class that orchestrates the hooks.
     */
    public function get_loader() {
        return $this->loader;
    }

    /**
     * Retrieve the version number of the plugin.
     */
    public function get_version() {
        return $this->version;
    }
}
