<?php
/**
 * iHomeFinder IDX Integration
 * Automatically detects and uses iHomeFinder Optima Express shortcodes.
 */
class AI_Realty_iHomeFinder_Integration {

    private $api_key;
    private $is_active;

    public function __construct() {
        $this->api_key = get_option('ai_realty_ihomefinder_key', '');
        $this->is_active = $this->check_if_active();
    }

    /**
     * Check if iHomeFinder is installed and active.
     */
    private function check_if_active() {
        return is_plugin_active('optima-express/optima-express.php') ||
               function_exists('ihf_insert_shortcode');
    }

    /**
     * Check if integration is configured.
     */
    public function is_configured() {
        return $this->is_active && !empty($this->api_key);
    }

    /**
     * Get available iHomeFinder shortcodes.
     */
    public function get_available_shortcodes() {
        if (!$this->is_active) {
            return array();
        }

        return array(
            'quick_search' => array(
                'shortcode' => '[ihf-quick-search]',
                'description' => 'Quick property search form',
                'page' => 'home'
            ),
            'property_search' => array(
                'shortcode' => '[ihf-property-search]',
                'description' => 'Advanced property search',
                'page' => 'search'
            ),
            'property_gallery' => array(
                'shortcode' => '[ihf-property-gallery]',
                'description' => 'Property gallery/listings',
                'page' => 'listings'
            ),
            'featured_listings' => array(
                'shortcode' => '[ihf-featured-listings]',
                'description' => 'Featured properties',
                'page' => 'home'
            ),
            'open_homes' => array(
                'shortcode' => '[ihf-open-homes]',
                'description' => 'Open houses',
                'page' => 'listings'
            ),
            'sold_properties' => array(
                'shortcode' => '[ihf-sold-properties]',
                'description' => 'Recently sold properties',
                'page' => 'listings'
            ),
            'home_valuation' => array(
                'shortcode' => '[ihf-home-valuation]',
                'description' => 'Home value estimator',
                'page' => 'valuation'
            ),
            'market_report' => array(
                'shortcode' => '[ihf-market-report]',
                'description' => 'MarketBoost market reports',
                'page' => 'market-report'
            ),
            'contact_form' => array(
                'shortcode' => '[ihf-contact-form]',
                'description' => 'IDX contact form',
                'page' => 'contact'
            ),
        );
    }

    /**
     * Get shortcode for a specific page type.
     */
    public function get_shortcode_for_page($page_type) {
        $shortcodes = $this->get_available_shortcodes();

        foreach ($shortcodes as $key => $data) {
            if ($data['page'] === $page_type) {
                return $data['shortcode'];
            }
        }

        return '';
    }

    /**
     * Inject agent ID into IDX lead forms.
     */
    public function inject_agent_id() {
        $attribution = new AI_Realty_Agent_Attribution();
        $agent_id = $attribution->get_agent_id();

        if (empty($agent_id)) {
            return;
        }

        // Add JavaScript to inject agent ID into iHomeFinder forms
        add_action('wp_footer', function() use ($agent_id) {
            ?>
            <script type="text/javascript">
            (function($) {
                $(document).ready(function() {
                    // Wait for iHomeFinder forms to load
                    setTimeout(function() {
                        // Add hidden field to all iHomeFinder forms
                        $('form[id^="ihf"]').each(function() {
                            if (!$(this).find('input[name="agent_id"]').length) {
                                $(this).append('<input type="hidden" name="agent_id" value="<?php echo esc_js($agent_id); ?>" />');
                            }
                        });
                    }, 1000);
                });
            })(jQuery);
            </script>
            <?php
        });
    }

    /**
     * Get IDX documentation link.
     */
    public function get_documentation_url() {
        return 'https://help.diversesolutions.com/optima-express/';
    }

    /**
     * Retrieve property data from iHomeFinder API.
     */
    public function get_property_data($property_id) {
        if (!$this->is_configured()) {
            return false;
        }

        // iHomeFinder API endpoint
        $api_url = "https://api.ihomefinder.com/properties/{$property_id}?apiKey={$this->api_key}";

        $response = wp_remote_get($api_url);

        if (is_wp_error($response)) {
            error_log('iHomeFinder API Error: ' . $response->get_error_message());
            return false;
        }

        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }

    /**
     * Get lead capture settings.
     */
    public function get_lead_settings() {
        return array(
            'capture_on_listing_view' => true,
            'capture_on_search' => true,
            'capture_on_save_search' => true,
            'capture_on_valuation' => true,
        );
    }
}
