<?php
/**
 * Admin Settings Template
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}
?>

<div class="wrap ai-realty-settings">
    <h1><?php echo esc_html(get_admin_page_title()); ?></h1>

    <form method="post" action="options.php">
        <?php
        settings_fields('ai_realty_autogen_options');
        do_settings_sections('ai-realty-autogen-settings');
        submit_button('Save Settings');
        ?>
    </form>

    <div class="ai-realty-card" style="margin-top: 30px;">
        <h2>🔐 API Key Setup Instructions</h2>

        <div class="api-instructions">
            <h3>Unsplash API (Free Images)</h3>
            <ol>
                <li>Sign up at <a href="https://unsplash.com/developers" target="_blank">unsplash.com/developers</a></li>
                <li>Create a new application</li>
                <li>Copy your Access Key</li>
                <li>Paste it in the Unsplash API Key field above</li>
            </ol>

            <h3>iHomeFinder (IDX Integration)</h3>
            <ol>
                <li>Install the "Optima Express" plugin from WordPress.org</li>
                <li>Sign up for an iHomeFinder account</li>
                <li>Get your API key from your iHomeFinder dashboard</li>
                <li>Configure Optima Express plugin with your credentials</li>
            </ol>

            <h3>GoHighLevel (CRM Integration)</h3>
            <ol>
                <li>Log in to your GoHighLevel account</li>
                <li>Go to Settings → API</li>
                <li>Create a new API key</li>
                <li>Copy your Location ID from Settings → Business Profile</li>
                <li>Paste both values above</li>
            </ol>
        </div>
    </div>

    <div class="ai-realty-card">
        <h2>🧪 Test Connections</h2>
        <p>Test your API integrations to ensure they're working correctly.</p>

        <button type="button" class="button" id="test-ghl-connection">
            <span class="dashicons dashicons-cloud"></span> Test GoHighLevel Connection
        </button>

        <div id="test-results" style="margin-top: 20px;"></div>
    </div>
</div>

<style>
.ai-realty-card {
    background: white;
    border: 1px solid #ccd0d4;
    border-radius: 4px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 1px 1px rgba(0,0,0,.04);
}

.ai-realty-card h2 {
    margin-top: 0;
}

.api-instructions h3 {
    margin-top: 20px;
    color: #2271b1;
}

.api-instructions ol {
    margin-left: 20px;
}
</style>

<script>
jQuery(document).ready(function($) {
    $('#test-ghl-connection').on('click', function() {
        var button = $(this);
        button.prop('disabled', true).text('Testing...');

        $.ajax({
            url: aiRealtyAutogen.ajax_url,
            method: 'POST',
            data: {
                action: 'test_ghl_connection',
                nonce: aiRealtyAutogen.nonce
            },
            success: function(response) {
                button.prop('disabled', false).html('<span class="dashicons dashicons-cloud"></span> Test GoHighLevel Connection');

                if (response.success) {
                    $('#test-results').html('<div class="notice notice-success"><p>' + response.data.message + '</p></div>');
                } else {
                    $('#test-results').html('<div class="notice notice-error"><p>' + response.data.message + '</p></div>');
                }
            },
            error: function() {
                button.prop('disabled', false).html('<span class="dashicons dashicons-cloud"></span> Test GoHighLevel Connection');
                $('#test-results').html('<div class="notice notice-error"><p>Connection test failed.</p></div>');
            }
        });
    });
});
</script>
