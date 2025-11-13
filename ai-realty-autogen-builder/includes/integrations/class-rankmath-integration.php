<?php
/**
 * Rank Math SEO Integration
 * Automatically configures SEO settings for pages and posts.
 */
class AI_Realty_RankMath_Integration {

    public function __construct() {
        // Hook into Rank Math if active
        if ($this->is_active()) {
            add_action('init', array($this, 'init'));
        }
    }

    /**
     * Check if Rank Math is active.
     */
    public function is_active() {
        return is_plugin_active('seo-by-rank-math/rank-math.php') && class_exists('RankMath');
    }

    /**
     * Initialize Rank Math integration.
     */
    public function init() {
        // Additional initialization if needed
    }

    /**
     * Set SEO metadata for a post/page.
     */
    public function set_seo_metadata($post_id, $data) {
        if (!$this->is_active()) {
            return false;
        }

        // Set title
        if (isset($data['title'])) {
            update_post_meta($post_id, 'rank_math_title', $data['title']);
        }

        // Set description
        if (isset($data['description'])) {
            update_post_meta($post_id, 'rank_math_description', $data['description']);
        }

        // Set focus keyword
        if (isset($data['focus_keyword'])) {
            update_post_meta($post_id, 'rank_math_focus_keyword', $data['focus_keyword']);
        }

        // Set robots meta
        if (isset($data['robots'])) {
            update_post_meta($post_id, 'rank_math_robots', $data['robots']);
        }

        // Set canonical URL
        if (isset($data['canonical'])) {
            update_post_meta($post_id, 'rank_math_canonical_url', $data['canonical']);
        }

        return true;
    }

    /**
     * Generate SEO-friendly metadata for real estate pages.
     */
    public function generate_real_estate_seo($post_id, $page_type) {
        $city = get_option('ai_realty_default_city', 'Austin');
        $state = get_option('ai_realty_default_state', 'TX');

        $seo_data = array();

        switch ($page_type) {
            case 'home':
                $seo_data = array(
                    'title' => "{$city} Real Estate | Homes for Sale in {$city}, {$state}",
                    'description' => "Find your dream home in {$city}, {$state}. Browse houses, condos, and properties for sale. Expert local real estate agents ready to help.",
                    'focus_keyword' => "{$city} real estate",
                );
                break;

            case 'listings':
                $seo_data = array(
                    'title' => "Properties for Sale in {$city}, {$state} | {$city} Real Estate",
                    'description' => "Browse all available properties for sale in {$city}. Updated daily with new listings, photos, and virtual tours.",
                    'focus_keyword' => "{$city} homes for sale",
                );
                break;

            case 'agents':
                $seo_data = array(
                    'title' => "Our Real Estate Agents | {$city} Realtors",
                    'description' => "Meet our experienced real estate agents serving {$city} and surrounding areas. Expert local knowledge and personalized service.",
                    'focus_keyword' => "{$city} real estate agents",
                );
                break;

            case 'contact':
                $seo_data = array(
                    'title' => "Contact Us | {$city} Real Estate",
                    'description' => "Get in touch with our {$city} real estate team. We're here to answer your questions and help you find your perfect home.",
                    'focus_keyword' => "contact {$city} realtor",
                );
                break;

            case 'blog':
                $seo_data = array(
                    'title' => "{$city} Real Estate Blog | Market News & Home Buying Tips",
                    'description' => "Stay informed about the {$city} real estate market. Tips for buyers and sellers, market updates, and local neighborhood guides.",
                    'focus_keyword' => "{$city} real estate blog",
                );
                break;
        }

        return $this->set_seo_metadata($post_id, $seo_data);
    }

    /**
     * Configure Rank Math sitemap settings.
     */
    public function configure_sitemap() {
        if (!$this->is_active()) {
            return false;
        }

        // Enable HTML sitemap
        update_option('rank_math_sitemap_html', true);

        // Enable XML sitemap
        update_option('rank_math_sitemap_xml', true);

        return true;
    }

    /**
     * Set up schema markup for real estate.
     */
    public function setup_real_estate_schema($post_id) {
        if (!$this->is_active()) {
            return false;
        }

        // Configure local business schema
        $schema = array(
            '@context' => 'https://schema.org',
            '@type' => 'RealEstateAgent',
            'name' => get_option('blogname'),
            'description' => get_option('blogdescription'),
            'url' => home_url(),
        );

        update_post_meta($post_id, 'rank_math_schema_RealEstateAgent', $schema);

        return true;
    }

    /**
     * Optimize all pages created by the builder.
     */
    public function optimize_all_pages() {
        if (!$this->is_active()) {
            return false;
        }

        $pages = array(
            'home' => 'Home',
            'listings' => 'Properties',
            'agents' => 'Our Agents',
            'contact' => 'Contact Us',
            'blog' => 'Blog',
        );

        foreach ($pages as $type => $title) {
            $page = get_page_by_title($title);
            if ($page) {
                $this->generate_real_estate_seo($page->ID, $type);
            }
        }

        return true;
    }
}
