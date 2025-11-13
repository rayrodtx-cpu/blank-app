<?php
/**
 * Elementor Page Builder Integration
 * Provides enhanced page building capabilities.
 */
class AI_Realty_Elementor_Integration {

    public function __construct() {
        // Hook into Elementor if active
        if ($this->is_active()) {
            add_action('elementor/init', array($this, 'init'));
        }
    }

    /**
     * Check if Elementor is active.
     */
    public function is_active() {
        return is_plugin_active('elementor/elementor.php') && defined('ELEMENTOR_VERSION');
    }

    /**
     * Initialize Elementor integration.
     */
    public function init() {
        // Register custom Elementor widgets if needed
        add_action('elementor/widgets/widgets_registered', array($this, 'register_widgets'));
    }

    /**
     * Register custom Elementor widgets.
     */
    public function register_widgets() {
        // Custom widgets would be registered here
        // For example: property listings widget, agent cards, etc.
    }

    /**
     * Create an Elementor page with template.
     */
    public function create_elementor_page($title, $template_data) {
        if (!$this->is_active()) {
            return false;
        }

        $page_data = array(
            'post_title' => $title,
            'post_content' => '',
            'post_status' => 'publish',
            'post_type' => 'page',
        );

        $page_id = wp_insert_post($page_data);

        if ($page_id) {
            // Set as Elementor page
            update_post_meta($page_id, '_elementor_edit_mode', 'builder');
            update_post_meta($page_id, '_elementor_data', json_encode($template_data));

            return $page_id;
        }

        return false;
    }

    /**
     * Get basic Elementor template for real estate homepage.
     */
    public function get_homepage_template() {
        return array(
            array(
                'id' => uniqid(),
                'elType' => 'section',
                'elements' => array(
                    array(
                        'id' => uniqid(),
                        'elType' => 'column',
                        'elements' => array(
                            array(
                                'id' => uniqid(),
                                'elType' => 'widget',
                                'widgetType' => 'heading',
                                'settings' => array(
                                    'title' => 'Find Your Dream Home',
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        );
    }

    /**
     * Get available Elementor templates.
     */
    public function get_templates() {
        if (!$this->is_active()) {
            return array();
        }

        $templates = get_posts(array(
            'post_type' => 'elementor_library',
            'posts_per_page' => -1,
        ));

        return $templates;
    }

    /**
     * Apply Elementor template to page.
     */
    public function apply_template_to_page($page_id, $template_id) {
        if (!$this->is_active()) {
            return false;
        }

        $template_data = get_post_meta($template_id, '_elementor_data', true);

        if ($template_data) {
            update_post_meta($page_id, '_elementor_data', $template_data);
            update_post_meta($page_id, '_elementor_edit_mode', 'builder');
            return true;
        }

        return false;
    }
}
