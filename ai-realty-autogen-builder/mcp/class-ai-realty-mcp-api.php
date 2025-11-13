<?php
/**
 * MCP (Model Context Protocol) REST API Handler
 * Exposes WordPress functionality to Claude AI via REST API.
 */
class AI_Realty_MCP_API {

    private $namespace = 'ai-builder/v1';

    /**
     * Register REST API routes.
     */
    public function register_routes() {
        // Build site endpoint
        register_rest_route($this->namespace, '/build-site', array(
            'methods' => 'POST',
            'callback' => array($this, 'build_site'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Update page endpoint
        register_rest_route($this->namespace, '/update-page', array(
            'methods' => 'POST',
            'callback' => array($this, 'update_page'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Create agent endpoint
        register_rest_route($this->namespace, '/create-agent', array(
            'methods' => 'POST',
            'callback' => array($this, 'create_agent'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Sync leads endpoint
        register_rest_route($this->namespace, '/sync-leads', array(
            'methods' => 'POST',
            'callback' => array($this, 'sync_leads'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Get status endpoint
        register_rest_route($this->namespace, '/status', array(
            'methods' => 'GET',
            'callback' => array($this, 'get_status'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Create page endpoint
        register_rest_route($this->namespace, '/create-page', array(
            'methods' => 'POST',
            'callback' => array($this, 'create_page'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Delete page endpoint
        register_rest_route($this->namespace, '/delete-page/(?P<id>\d+)', array(
            'methods' => 'DELETE',
            'callback' => array($this, 'delete_page'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Get leads endpoint
        register_rest_route($this->namespace, '/leads', array(
            'methods' => 'GET',
            'callback' => array($this, 'get_leads'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Get agents endpoint
        register_rest_route($this->namespace, '/agents', array(
            'methods' => 'GET',
            'callback' => array($this, 'get_agents'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Update settings endpoint
        register_rest_route($this->namespace, '/settings', array(
            'methods' => 'POST',
            'callback' => array($this, 'update_settings'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Get pages endpoint
        register_rest_route($this->namespace, '/pages', array(
            'methods' => 'GET',
            'callback' => array($this, 'get_pages'),
            'permission_callback' => array($this, 'check_permissions'),
        ));

        // Execute prompt endpoint (for autonomous building)
        register_rest_route($this->namespace, '/execute-prompt', array(
            'methods' => 'POST',
            'callback' => array($this, 'execute_prompt'),
            'permission_callback' => array($this, 'check_permissions'),
        ));
    }

    /**
     * Check API permissions.
     */
    public function check_permissions() {
        // Allow requests with valid nonce or from localhost
        if (current_user_can('manage_options')) {
            return true;
        }

        // Check for API key in header
        $api_key = get_option('ai_realty_api_key', '');
        $request_key = isset($_SERVER['HTTP_X_API_KEY']) ? $_SERVER['HTTP_X_API_KEY'] : '';

        if (!empty($api_key) && $api_key === $request_key) {
            return true;
        }

        // Allow from localhost for development
        if (isset($_SERVER['REMOTE_ADDR']) && in_array($_SERVER['REMOTE_ADDR'], array('127.0.0.1', '::1'))) {
            return true;
        }

        return new WP_Error(
            'rest_forbidden',
            'You do not have permission to access this endpoint.',
            array('status' => 401)
        );
    }

    /**
     * Build entire site from prompt.
     */
    public function build_site($request) {
        $params = $request->get_json_params();
        $prompt = isset($params['prompt']) ? sanitize_textarea_field($params['prompt']) : '';

        // Update prompt in settings
        if (!empty($prompt)) {
            update_option('ai_realty_site_prompt', $prompt);
        }

        // Initialize site builder
        $builder = new AI_Realty_Site_Builder($prompt);
        $result = $builder->build_site();

        return rest_ensure_response($result);
    }

    /**
     * Update existing page content.
     */
    public function update_page($request) {
        $params = $request->get_json_params();
        $page_id = isset($params['page_id']) ? intval($params['page_id']) : 0;
        $title = isset($params['title']) ? sanitize_text_field($params['title']) : '';
        $content = isset($params['content']) ? wp_kses_post($params['content']) : '';

        if (!$page_id && !empty($title)) {
            // Find page by title
            $page = get_page_by_title($title);
            if ($page) {
                $page_id = $page->ID;
            }
        }

        if (!$page_id) {
            return new WP_Error(
                'page_not_found',
                'Page not found.',
                array('status' => 404)
            );
        }

        $update_data = array(
            'ID' => $page_id,
        );

        if (!empty($title)) {
            $update_data['post_title'] = $title;
        }

        if (!empty($content)) {
            $update_data['post_content'] = $content;
        }

        $result = wp_update_post($update_data);

        if (is_wp_error($result)) {
            return $result;
        }

        return rest_ensure_response(array(
            'success' => true,
            'page_id' => $page_id,
            'message' => 'Page updated successfully.'
        ));
    }

    /**
     * Create new page.
     */
    public function create_page($request) {
        $params = $request->get_json_params();
        $title = isset($params['title']) ? sanitize_text_field($params['title']) : '';
        $content = isset($params['content']) ? wp_kses_post($params['content']) : '';
        $status = isset($params['status']) ? sanitize_text_field($params['status']) : 'publish';

        if (empty($title)) {
            return new WP_Error(
                'missing_title',
                'Page title is required.',
                array('status' => 400)
            );
        }

        $page_data = array(
            'post_title' => $title,
            'post_content' => $content,
            'post_status' => $status,
            'post_type' => 'page',
            'post_author' => 1,
        );

        $page_id = wp_insert_post($page_data);

        if (is_wp_error($page_id)) {
            return $page_id;
        }

        return rest_ensure_response(array(
            'success' => true,
            'page_id' => $page_id,
            'message' => 'Page created successfully.',
            'url' => get_permalink($page_id)
        ));
    }

    /**
     * Delete page.
     */
    public function delete_page($request) {
        $page_id = $request->get_param('id');

        $result = wp_delete_post($page_id, true);

        if (!$result) {
            return new WP_Error(
                'delete_failed',
                'Failed to delete page.',
                array('status' => 500)
            );
        }

        return rest_ensure_response(array(
            'success' => true,
            'message' => 'Page deleted successfully.'
        ));
    }

    /**
     * Create new agent.
     */
    public function create_agent($request) {
        $params = $request->get_json_params();

        $agent_data = array(
            'agent_id' => isset($params['agent_id']) ? sanitize_text_field($params['agent_id']) : 'agent' . time(),
            'name' => isset($params['name']) ? sanitize_text_field($params['name']) : '',
            'email' => isset($params['email']) ? sanitize_email($params['email']) : '',
            'phone' => isset($params['phone']) ? sanitize_text_field($params['phone']) : '',
            'bio' => isset($params['bio']) ? sanitize_textarea_field($params['bio']) : '',
            'photo_url' => isset($params['photo_url']) ? esc_url_raw($params['photo_url']) : '',
        );

        if (empty($agent_data['name']) || empty($agent_data['email'])) {
            return new WP_Error(
                'missing_data',
                'Agent name and email are required.',
                array('status' => 400)
            );
        }

        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_agents';

        $result = $wpdb->insert($table, $agent_data);

        if ($result) {
            return rest_ensure_response(array(
                'success' => true,
                'agent_id' => $agent_data['agent_id'],
                'message' => 'Agent created successfully.'
            ));
        }

        return new WP_Error(
            'create_failed',
            'Failed to create agent.',
            array('status' => 500)
        );
    }

    /**
     * Sync leads to GoHighLevel.
     */
    public function sync_leads($request) {
        $ghl = new AI_Realty_GoHighLevel_Integration();

        if (!$ghl->is_configured()) {
            return new WP_Error(
                'not_configured',
                'GoHighLevel is not configured.',
                array('status' => 400)
            );
        }

        $result = $ghl->sync_all_leads();

        return rest_ensure_response(array(
            'success' => true,
            'total' => $result['total'],
            'synced' => $result['synced'],
            'message' => "Synced {$result['synced']} of {$result['total']} leads."
        ));
    }

    /**
     * Get site status.
     */
    public function get_status($request) {
        $attribution = new AI_Realty_Agent_Attribution();

        $status = array(
            'build_status' => get_option('ai_realty_build_status', 'not_started'),
            'site_url' => home_url(),
            'site_title' => get_option('blogname'),
            'installed_plugins' => get_option('ai_realty_installed_plugins', array()),
            'total_leads' => $attribution->get_leads_count(),
            'total_agents' => $this->get_agents_count(),
            'total_pages' => wp_count_posts('page')->publish,
            'integrations' => array(
                'elementor' => is_plugin_active('elementor/elementor.php'),
                'rank_math' => is_plugin_active('seo-by-rank-math/rank-math.php'),
                'contact_form_7' => is_plugin_active('contact-form-7/wp-contact-form-7.php'),
                'wpforms' => is_plugin_active('wpforms-lite/wpforms.php'),
                'ihomefinder' => is_plugin_active('optima-express/optima-express.php'),
                'gohighlevel' => !empty(get_option('ai_realty_ghl_api_key')),
            ),
            'build_log' => get_option('ai_realty_build_log', array()),
        );

        return rest_ensure_response($status);
    }

    /**
     * Get all leads.
     */
    public function get_leads($request) {
        $limit = $request->get_param('limit') ?: 50;
        $offset = $request->get_param('offset') ?: 0;

        $attribution = new AI_Realty_Agent_Attribution();
        $leads = $attribution->get_all_leads($limit, $offset);

        return rest_ensure_response(array(
            'success' => true,
            'leads' => $leads,
            'total' => $attribution->get_leads_count()
        ));
    }

    /**
     * Get all agents.
     */
    public function get_agents($request) {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_agents';

        $agents = $wpdb->get_results("SELECT * FROM $table ORDER BY created_at DESC");

        return rest_ensure_response(array(
            'success' => true,
            'agents' => $agents
        ));
    }

    /**
     * Get agents count.
     */
    private function get_agents_count() {
        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_agents';

        return $wpdb->get_var("SELECT COUNT(*) FROM $table");
    }

    /**
     * Update settings.
     */
    public function update_settings($request) {
        $params = $request->get_json_params();

        foreach ($params as $key => $value) {
            $option_key = 'ai_realty_' . $key;
            update_option($option_key, sanitize_text_field($value));
        }

        return rest_ensure_response(array(
            'success' => true,
            'message' => 'Settings updated successfully.'
        ));
    }

    /**
     * Get all pages.
     */
    public function get_pages($request) {
        $pages = get_pages(array(
            'sort_column' => 'post_title',
            'sort_order' => 'ASC'
        ));

        $page_list = array();
        foreach ($pages as $page) {
            $page_list[] = array(
                'id' => $page->ID,
                'title' => $page->post_title,
                'slug' => $page->post_name,
                'url' => get_permalink($page->ID),
                'status' => $page->post_status,
            );
        }

        return rest_ensure_response(array(
            'success' => true,
            'pages' => $page_list
        ));
    }

    /**
     * Execute a natural language prompt.
     */
    public function execute_prompt($request) {
        $params = $request->get_json_params();
        $prompt = isset($params['prompt']) ? sanitize_textarea_field($params['prompt']) : '';

        if (empty($prompt)) {
            return new WP_Error(
                'missing_prompt',
                'Prompt is required.',
                array('status' => 400)
            );
        }

        // Log the prompt
        error_log("AI Realty Autogen: Executing prompt - {$prompt}");

        // For now, return a success message
        // In a full implementation, this would integrate with Claude API
        return rest_ensure_response(array(
            'success' => true,
            'message' => 'Prompt received and queued for processing.',
            'prompt' => $prompt
        ));
    }
}
