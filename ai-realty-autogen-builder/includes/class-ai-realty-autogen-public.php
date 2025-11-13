<?php
/**
 * The public-facing functionality of the plugin.
 */
class AI_Realty_Autogen_Public {

    private $plugin_name;
    private $version;

    public function __construct($plugin_name, $version) {
        $this->plugin_name = $plugin_name;
        $this->version = $version;
    }

    /**
     * Register the stylesheets for the public-facing side.
     */
    public function enqueue_styles() {
        wp_enqueue_style(
            $this->plugin_name,
            AI_REALTY_AUTOGEN_PLUGIN_URL . 'assets/css/ai-realty-autogen-public.css',
            array(),
            $this->version,
            'all'
        );
    }

    /**
     * Register the JavaScript for the public-facing side.
     */
    public function enqueue_scripts() {
        wp_enqueue_script(
            $this->plugin_name,
            AI_REALTY_AUTOGEN_PLUGIN_URL . 'assets/js/ai-realty-autogen-public.js',
            array('jquery'),
            $this->version,
            false
        );

        // Pass cookie settings to JS
        wp_localize_script(
            $this->plugin_name,
            'aiRealtyPublic',
            array(
                'cookie_name' => get_option('ai_realty_agent_cookie_name', 'agent_ref'),
                'cookie_expiry' => get_option('ai_realty_agent_cookie_expiry', 30)
            )
        );
    }
}
