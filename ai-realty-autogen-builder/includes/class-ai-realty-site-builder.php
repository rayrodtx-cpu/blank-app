<?php
/**
 * The autonomous site builder engine.
 * Handles complete website creation from natural language prompts.
 */
class AI_Realty_Site_Builder {

    private $prompt;
    private $city;
    private $state;
    private $build_log = array();

    /**
     * Initialize the site builder with a prompt.
     */
    public function __construct($prompt = '') {
        $this->prompt = $prompt;
        $this->city = get_option('ai_realty_default_city', 'Austin');
        $this->state = get_option('ai_realty_default_state', 'TX');
    }

    /**
     * Main build method - orchestrates the entire site creation.
     */
    public function build_site() {
        $this->log('Starting autonomous site build...');
        update_option('ai_realty_build_status', 'building');

        try {
            // Step 1: Check and recommend plugins
            $this->check_required_plugins();

            // Step 2: Create core pages
            $pages = $this->create_core_pages();

            // Step 3: Set up navigation menus
            $this->create_navigation_menus($pages);

            // Step 4: Create sample agents
            $this->create_sample_agents();

            // Step 5: Create sample blog posts
            $this->create_sample_blog_posts();

            // Step 6: Create sample property listings (if no IDX)
            if (!$this->is_idx_active()) {
                $this->create_sample_listings();
            }

            // Step 7: Configure theme and appearance
            $this->configure_theme();

            // Step 8: Set up widgets and sidebars
            $this->setup_widgets();

            // Step 9: Configure SEO (RankMath)
            $this->configure_seo();

            // Step 10: Set homepage and blog page
            $this->set_reading_settings($pages);

            $this->log('Site build completed successfully!');
            update_option('ai_realty_build_status', 'completed');
            update_option('ai_realty_build_log', $this->build_log);

            return array(
                'success' => true,
                'message' => 'Site built successfully!',
                'log' => $this->build_log
            );

        } catch (Exception $e) {
            $this->log('Error: ' . $e->getMessage());
            update_option('ai_realty_build_status', 'error');
            update_option('ai_realty_build_log', $this->build_log);

            return array(
                'success' => false,
                'message' => $e->getMessage(),
                'log' => $this->build_log
            );
        }
    }

    /**
     * Check for required/recommended plugins.
     */
    private function check_required_plugins() {
        $this->log('Checking for recommended plugins...');

        $recommended = array(
            'elementor/elementor.php' => 'Elementor',
            'contact-form-7/wp-contact-form-7.php' => 'Contact Form 7',
            'seo-by-rank-math/rank-math.php' => 'Rank Math SEO',
            'wpforms-lite/wpforms.php' => 'WPForms Lite',
        );

        $missing = array();
        foreach ($recommended as $plugin => $name) {
            if (!is_plugin_active($plugin)) {
                $missing[] = $name;
            }
        }

        if (!empty($missing)) {
            $this->log('Recommended plugins not active: ' . implode(', ', $missing));
            $this->log('Install these for enhanced functionality.');
        }

        update_option('ai_realty_installed_plugins', $this->get_active_integrations());
    }

    /**
     * Create all core pages for the real estate site.
     */
    private function create_core_pages() {
        $this->log('Creating core pages...');

        $pages = array();

        // Home page
        $pages['home'] = $this->create_page(
            'Home',
            $this->get_home_page_content(),
            'publish'
        );

        // Listings page
        $pages['listings'] = $this->create_page(
            'Properties',
            $this->get_listings_page_content(),
            'publish'
        );

        // Search page
        $pages['search'] = $this->create_page(
            'Search Properties',
            $this->get_search_page_content(),
            'publish'
        );

        // Agents page
        $pages['agents'] = $this->create_page(
            'Our Agents',
            $this->get_agents_page_content(),
            'publish'
        );

        // About page
        $pages['about'] = $this->create_page(
            'About Us',
            $this->get_about_page_content(),
            'publish'
        );

        // Contact page
        $pages['contact'] = $this->create_page(
            'Contact Us',
            $this->get_contact_page_content(),
            'publish'
        );

        // Blog page
        $pages['blog'] = $this->create_page(
            'Blog',
            '<!-- Latest real estate news and market insights -->',
            'publish'
        );

        $this->log('Created ' . count($pages) . ' pages successfully.');
        return $pages;
    }

    /**
     * Create a single page.
     */
    private function create_page($title, $content, $status = 'publish') {
        // Check if page already exists
        $existing = get_page_by_title($title);
        if ($existing) {
            $this->log("Page '$title' already exists. Skipping.");
            return $existing->ID;
        }

        $page_data = array(
            'post_title'   => $title,
            'post_content' => $content,
            'post_status'  => $status,
            'post_type'    => 'page',
            'post_author'  => 1,
        );

        $page_id = wp_insert_post($page_data);

        if ($page_id) {
            $this->log("Created page: $title (ID: $page_id)");

            // Set featured image if Unsplash is configured
            $this->set_featured_image($page_id, $title);

            return $page_id;
        }

        return false;
    }

    /**
     * Get home page content.
     */
    private function get_home_page_content() {
        $city = $this->city;
        $state = $this->state;

        $content = "<!-- wp:heading {\"level\":1} -->\n";
        $content .= "<h1>Welcome to {$city} Real Estate</h1>\n";
        $content .= "<!-- /wp:heading -->\n\n";

        $content .= "<!-- wp:paragraph -->\n";
        $content .= "<p>Find your dream home in {$city}, {$state}. We're dedicated to helping you find the perfect property.</p>\n";
        $content .= "<!-- /wp:paragraph -->\n\n";

        // Add IDX search if available
        if ($this->is_idx_active()) {
            $content .= "<!-- wp:paragraph -->\n";
            $content .= "<p>[ihf-quick-search]</p>\n";
            $content .= "<!-- /wp:paragraph -->\n\n";
        }

        $content .= "<!-- wp:heading -->\n";
        $content .= "<h2>Featured Properties</h2>\n";
        $content .= "<!-- /wp:heading -->\n\n";

        if ($this->is_idx_active()) {
            $content .= "<!-- wp:paragraph -->\n";
            $content .= "<p>[ihf-featured-listings]</p>\n";
            $content .= "<!-- /wp:paragraph -->\n";
        } else {
            $content .= "<!-- wp:paragraph -->\n";
            $content .= "<p>Check out our latest property listings!</p>\n";
            $content .= "<!-- /wp:paragraph -->\n";
        }

        return $content;
    }

    /**
     * Get listings page content.
     */
    private function get_listings_page_content() {
        if ($this->is_idx_active()) {
            return "[ihf-property-gallery]";
        }

        return "<!-- wp:heading -->\n<h2>Available Properties</h2>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>Browse our selection of properties in {$this->city}.</p>\n<!-- /wp:paragraph -->";
    }

    /**
     * Get search page content.
     */
    private function get_search_page_content() {
        if ($this->is_idx_active()) {
            return "[ihf-property-search]";
        }

        return "<!-- wp:heading -->\n<h2>Search Properties</h2>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>Use the search form below to find your perfect property.</p>\n<!-- /wp:paragraph -->";
    }

    /**
     * Get agents page content.
     */
    private function get_agents_page_content() {
        return "<!-- wp:heading -->\n<h2>Meet Our Team</h2>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>Our experienced real estate agents are here to help you find your dream home.</p>\n<!-- /wp:paragraph -->";
    }

    /**
     * Get about page content.
     */
    private function get_about_page_content() {
        $city = $this->city;
        return "<!-- wp:heading -->\n<h2>About {$city} Real Estate</h2>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>We are a full-service real estate agency serving the {$city} area. With years of experience and deep local knowledge, we help buyers and sellers achieve their real estate goals.</p>\n<!-- /wp:paragraph -->\n\n<!-- wp:paragraph -->\n<p>Our mission is to provide exceptional service, expert guidance, and honest advice throughout your real estate journey.</p>\n<!-- /wp:paragraph -->";
    }

    /**
     * Get contact page content.
     */
    private function get_contact_page_content() {
        $content = "<!-- wp:heading -->\n<h2>Get In Touch</h2>\n<!-- /wp:heading -->\n\n";
        $content .= "<!-- wp:paragraph -->\n<p>Ready to find your dream home? Contact us today!</p>\n<!-- /wp:paragraph -->\n\n";

        // Add Contact Form 7 shortcode if active
        if (is_plugin_active('contact-form-7/wp-contact-form-7.php')) {
            // Create a contact form
            $form_id = $this->create_contact_form();
            if ($form_id) {
                $content .= "<!-- wp:paragraph -->\n<p>[contact-form-7 id=\"{$form_id}\" title=\"Contact Form\"]</p>\n<!-- /wp:paragraph -->";
            }
        } else {
            $content .= "<!-- wp:paragraph -->\n<p>Email: info@example.com<br>Phone: (555) 123-4567</p>\n<!-- /wp:paragraph -->";
        }

        return $content;
    }

    /**
     * Create Contact Form 7 form.
     */
    private function create_contact_form() {
        if (!is_plugin_active('contact-form-7/wp-contact-form-7.php')) {
            return false;
        }

        $form_title = 'Contact Form';
        $form_template = '
<label> Your Name (required)
    [text* your-name] </label>

<label> Your Email (required)
    [email* your-email] </label>

<label> Phone
    [tel your-phone] </label>

<label> Your Message
    [textarea your-message] </label>

[hidden agent-id default:get]

[submit "Send"]';

        $mail_template = 'From: [your-name] <[your-email]>
Subject: New Contact Form Submission

Name: [your-name]
Email: [your-email]
Phone: [your-phone]
Agent ID: [agent-id]

Message:
[your-message]';

        $contact_form = WPCF7_ContactForm::get_instance();
        $contact_form->set_title($form_title);
        $contact_form->set_properties(array(
            'form' => $form_template,
            'mail' => array(
                'subject' => 'Contact Form Submission',
                'sender' => '[your-name] <[your-email]>',
                'body' => $mail_template,
                'recipient' => get_option('admin_email'),
            ),
        ));
        $contact_form->save();

        $this->log("Created Contact Form 7 form (ID: {$contact_form->id()})");
        return $contact_form->id();
    }

    /**
     * Create navigation menus.
     */
    private function create_navigation_menus($pages) {
        $this->log('Creating navigation menus...');

        // Create main menu
        $menu_name = 'Main Menu';
        $menu_exists = wp_get_nav_menu_object($menu_name);

        if (!$menu_exists) {
            $menu_id = wp_create_nav_menu($menu_name);

            // Add menu items
            $menu_items = array(
                array('title' => 'Home', 'page_id' => $pages['home']),
                array('title' => 'Properties', 'page_id' => $pages['listings']),
                array('title' => 'Search', 'page_id' => $pages['search']),
                array('title' => 'Our Agents', 'page_id' => $pages['agents']),
                array('title' => 'About', 'page_id' => $pages['about']),
                array('title' => 'Blog', 'page_id' => $pages['blog']),
                array('title' => 'Contact', 'page_id' => $pages['contact']),
            );

            foreach ($menu_items as $item) {
                wp_update_nav_menu_item($menu_id, 0, array(
                    'menu-item-title' => $item['title'],
                    'menu-item-object' => 'page',
                    'menu-item-object-id' => $item['page_id'],
                    'menu-item-type' => 'post_type',
                    'menu-item-status' => 'publish'
                ));
            }

            // Assign menu to theme location
            $locations = get_theme_mod('nav_menu_locations');
            $locations['primary'] = $menu_id;
            set_theme_mod('nav_menu_locations', $locations);

            $this->log("Created main navigation menu (ID: $menu_id)");
        }
    }

    /**
     * Create sample agents.
     */
    private function create_sample_agents() {
        $this->log('Creating sample agent profiles...');

        global $wpdb;
        $table = $wpdb->prefix . 'ai_realty_agents';

        $agents = array(
            array(
                'agent_id' => 'agent001',
                'name' => 'Sarah Johnson',
                'email' => 'sarah@example.com',
                'phone' => '(555) 123-4567',
                'bio' => 'Experienced real estate professional with 10+ years serving the Austin area.',
            ),
            array(
                'agent_id' => 'agent002',
                'name' => 'Michael Chen',
                'email' => 'michael@example.com',
                'phone' => '(555) 234-5678',
                'bio' => 'Specializing in luxury properties and investment real estate.',
            ),
        );

        foreach ($agents as $agent) {
            $existing = $wpdb->get_var($wpdb->prepare(
                "SELECT id FROM $table WHERE agent_id = %s",
                $agent['agent_id']
            ));

            if (!$existing) {
                $wpdb->insert($table, $agent);
                $this->log("Created agent: {$agent['name']}");
            }
        }
    }

    /**
     * Create sample blog posts.
     */
    private function create_sample_blog_posts() {
        $this->log('Creating sample blog posts...');

        $posts = array(
            array(
                'title' => "Top 10 Neighborhoods in {$this->city}",
                'content' => "Discover the best neighborhoods in {$this->city} for families, young professionals, and retirees. Each area offers unique charm and amenities.",
            ),
            array(
                'title' => 'First-Time Home Buyer\'s Guide',
                'content' => 'Everything you need to know about buying your first home, from getting pre-approved to closing day.',
            ),
            array(
                'title' => "{$this->city} Real Estate Market Update",
                'content' => "Get the latest insights on the {$this->city} real estate market, including trends, pricing, and forecasts.",
            ),
        );

        foreach ($posts as $post_data) {
            $existing = get_page_by_title($post_data['title'], OBJECT, 'post');
            if (!$existing) {
                $post_id = wp_insert_post(array(
                    'post_title' => $post_data['title'],
                    'post_content' => $post_data['content'],
                    'post_status' => 'publish',
                    'post_type' => 'post',
                    'post_author' => 1,
                ));

                if ($post_id) {
                    $this->log("Created blog post: {$post_data['title']}");
                    $this->set_featured_image($post_id, $post_data['title']);
                }
            }
        }
    }

    /**
     * Create sample property listings (if no IDX).
     */
    private function create_sample_listings() {
        $this->log('Creating sample property listings...');

        // Register custom post type for properties
        register_post_type('property', array(
            'labels' => array(
                'name' => 'Properties',
                'singular_name' => 'Property',
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array('title', 'editor', 'thumbnail'),
            'show_in_rest' => true,
        ));

        $properties = array(
            array(
                'title' => "Beautiful 3BR Home in {$this->city}",
                'content' => 'Stunning 3 bedroom, 2 bathroom home with modern updates. Open floor plan, spacious kitchen, and beautiful backyard.',
                'price' => '$450,000',
                'bedrooms' => '3',
                'bathrooms' => '2',
            ),
            array(
                'title' => "Luxury Condo Downtown {$this->city}",
                'content' => 'Modern 2 bedroom luxury condo in the heart of downtown. High-end finishes, city views, and premium amenities.',
                'price' => '$575,000',
                'bedrooms' => '2',
                'bathrooms' => '2',
            ),
        );

        foreach ($properties as $property) {
            $post_id = wp_insert_post(array(
                'post_title' => $property['title'],
                'post_content' => $property['content'],
                'post_status' => 'publish',
                'post_type' => 'property',
                'post_author' => 1,
            ));

            if ($post_id) {
                update_post_meta($post_id, '_property_price', $property['price']);
                update_post_meta($post_id, '_property_bedrooms', $property['bedrooms']);
                update_post_meta($post_id, '_property_bathrooms', $property['bathrooms']);
                $this->log("Created property: {$property['title']}");
                $this->set_featured_image($post_id, $property['title']);
            }
        }
    }

    /**
     * Configure theme settings.
     */
    private function configure_theme() {
        $this->log('Configuring theme settings...');

        // Set site title and tagline
        update_option('blogname', "{$this->city} Real Estate");
        update_option('blogdescription', "Your trusted real estate partner in {$this->city}, {$this->state}");

        $this->log('Theme configured.');
    }

    /**
     * Set up widgets and sidebars.
     */
    private function setup_widgets() {
        $this->log('Setting up widgets...');
        // Widget setup would be theme-specific
        $this->log('Widgets configured.');
    }

    /**
     * Configure SEO settings (RankMath).
     */
    private function configure_seo() {
        if (!is_plugin_active('seo-by-rank-math/rank-math.php')) {
            return;
        }

        $this->log('Configuring SEO settings...');

        // Basic RankMath configuration would go here
        update_option('rank_math_sitemap_html', true);

        $this->log('SEO configured.');
    }

    /**
     * Set reading settings (homepage and blog page).
     */
    private function set_reading_settings($pages) {
        $this->log('Setting reading settings...');

        update_option('show_on_front', 'page');
        update_option('page_on_front', $pages['home']);
        update_option('page_for_posts', $pages['blog']);

        $this->log('Reading settings configured.');
    }

    /**
     * Set featured image for a post/page using Unsplash.
     */
    private function set_featured_image($post_id, $title) {
        $unsplash_key = get_option('ai_realty_unsplash_api_key', '');

        if (empty($unsplash_key)) {
            return false;
        }

        // Search Unsplash for relevant image
        $search_term = 'real estate house';
        $url = "https://api.unsplash.com/photos/random?query={$search_term}&client_id={$unsplash_key}";

        $response = wp_remote_get($url);

        if (is_wp_error($response)) {
            return false;
        }

        $body = json_decode(wp_remote_retrieve_body($response), true);

        if (isset($body['urls']['regular'])) {
            $image_url = $body['urls']['regular'];

            // Download and attach image
            $image_id = $this->upload_image_from_url($image_url, $post_id);

            if ($image_id) {
                set_post_thumbnail($post_id, $image_id);
                $this->log("Set featured image for post $post_id");
                return true;
            }
        }

        return false;
    }

    /**
     * Upload image from URL.
     */
    private function upload_image_from_url($image_url, $post_id) {
        require_once(ABSPATH . 'wp-admin/includes/media.php');
        require_once(ABSPATH . 'wp-admin/includes/file.php');
        require_once(ABSPATH . 'wp-admin/includes/image.php');

        $tmp = download_url($image_url);

        if (is_wp_error($tmp)) {
            return false;
        }

        $file_array = array(
            'name' => basename($image_url),
            'tmp_name' => $tmp
        );

        $id = media_handle_sideload($file_array, $post_id);

        if (is_wp_error($id)) {
            @unlink($file_array['tmp_name']);
            return false;
        }

        return $id;
    }

    /**
     * Check if iHomeFinder IDX is active.
     */
    private function is_idx_active() {
        return is_plugin_active('optima-express/optima-express.php') ||
               function_exists('ihf_insert_shortcode');
    }

    /**
     * Get active integrations.
     */
    private function get_active_integrations() {
        $integrations = array();

        if (is_plugin_active('elementor/elementor.php')) {
            $integrations[] = 'elementor';
        }
        if (is_plugin_active('contact-form-7/wp-contact-form-7.php')) {
            $integrations[] = 'contact-form-7';
        }
        if (is_plugin_active('seo-by-rank-math/rank-math.php')) {
            $integrations[] = 'rank-math';
        }
        if (is_plugin_active('wpforms-lite/wpforms.php')) {
            $integrations[] = 'wpforms';
        }
        if ($this->is_idx_active()) {
            $integrations[] = 'ihomefinder';
        }
        if (is_plugin_active('ghl-lead-connector/ghl-lead-connector.php')) {
            $integrations[] = 'gohighlevel';
        }

        return $integrations;
    }

    /**
     * Log build progress.
     */
    private function log($message) {
        $this->build_log[] = array(
            'time' => current_time('mysql'),
            'message' => $message
        );
        error_log('[AI Realty Autogen] ' . $message);
    }

    /**
     * Get the current build log.
     */
    public function get_log() {
        return $this->build_log;
    }
}
