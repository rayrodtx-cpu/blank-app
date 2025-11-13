<?php
/**
 * Admin Dashboard Template
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

$build_status = get_option('ai_realty_build_status', 'not_started');
$attribution = new AI_Realty_Agent_Attribution();
$total_leads = $attribution->get_leads_count();
$site_prompt = get_option('ai_realty_site_prompt', '');

global $wpdb;
$agents_table = $wpdb->prefix . 'ai_realty_agents';
$total_agents = $wpdb->get_var("SELECT COUNT(*) FROM $agents_table");
?>

<div class="wrap ai-realty-dashboard">
    <h1><?php echo esc_html(get_admin_page_title()); ?></h1>

    <div class="ai-realty-header">
        <p class="description">
            Autonomous AI-powered real estate website builder. Create complete websites from natural language prompts.
        </p>
    </div>

    <!-- Build Status Card -->
    <div class="ai-realty-card">
        <h2>🏗️ Site Build Status</h2>
        <div class="status-indicator status-<?php echo esc_attr($build_status); ?>">
            <?php
            switch ($build_status) {
                case 'not_started':
                    echo '<span class="dashicons dashicons-info"></span> Not Started';
                    break;
                case 'building':
                    echo '<span class="dashicons dashicons-update"></span> Building...';
                    break;
                case 'completed':
                    echo '<span class="dashicons dashicons-yes"></span> Completed';
                    break;
                case 'error':
                    echo '<span class="dashicons dashicons-warning"></span> Error';
                    break;
            }
            ?>
        </div>

        <div class="build-actions" style="margin-top: 20px;">
            <h3>Build Your Real Estate Site</h3>
            <p>Enter a prompt describing your ideal real estate website, or use the default settings:</p>

            <textarea id="ai-realty-prompt" rows="4" style="width: 100%; max-width: 600px;" placeholder="Example: Build a real estate website for Austin agents with IDX listings, blog, lead capture forms, and agent profiles."><?php echo esc_textarea($site_prompt); ?></textarea>

            <div style="margin-top: 10px;">
                <button type="button" class="button button-primary button-large" id="ai-realty-build-btn">
                    <span class="dashicons dashicons-admin-site-alt3"></span> Build Site Now
                </button>
                <button type="button" class="button button-secondary" id="ai-realty-rebuild-btn">
                    <span class="dashicons dashicons-update"></span> Rebuild Site
                </button>
            </div>

            <div id="ai-realty-build-progress" style="display: none; margin-top: 20px;">
                <div class="progress-bar">
                    <div class="progress-fill"></div>
                </div>
                <p class="progress-message">Building your site...</p>
            </div>

            <div id="ai-realty-build-log" style="margin-top: 20px; display: none;">
                <h4>Build Log:</h4>
                <div class="build-log-content" style="background: #f5f5f5; padding: 10px; max-height: 300px; overflow-y: auto; font-family: monospace; font-size: 12px;"></div>
            </div>
        </div>
    </div>

    <!-- Stats Cards -->
    <div class="ai-realty-stats">
        <div class="stat-card">
            <div class="stat-icon"><span class="dashicons dashicons-admin-page"></span></div>
            <div class="stat-content">
                <h3><?php echo wp_count_posts('page')->publish; ?></h3>
                <p>Pages</p>
            </div>
        </div>

        <div class="stat-card">
            <div class="stat-icon"><span class="dashicons dashicons-email"></span></div>
            <div class="stat-content">
                <h3><?php echo $total_leads; ?></h3>
                <p>Leads</p>
            </div>
        </div>

        <div class="stat-card">
            <div class="stat-icon"><span class="dashicons dashicons-groups"></span></div>
            <div class="stat-content">
                <h3><?php echo $total_agents; ?></h3>
                <p>Agents</p>
            </div>
        </div>

        <div class="stat-card">
            <div class="stat-icon"><span class="dashicons dashicons-admin-post"></span></div>
            <div class="stat-content">
                <h3><?php echo wp_count_posts('post')->publish; ?></h3>
                <p>Blog Posts</p>
            </div>
        </div>
    </div>

    <!-- Quick Actions -->
    <div class="ai-realty-card">
        <h2>⚡ Quick Actions</h2>
        <div class="quick-actions">
            <a href="<?php echo admin_url('admin.php?page=ai-realty-autogen-settings'); ?>" class="quick-action-btn">
                <span class="dashicons dashicons-admin-settings"></span>
                Configure Settings
            </a>
            <a href="<?php echo admin_url('admin.php?page=ai-realty-autogen-leads'); ?>" class="quick-action-btn">
                <span class="dashicons dashicons-email-alt"></span>
                View Leads
            </a>
            <a href="<?php echo admin_url('admin.php?page=ai-realty-autogen-agents'); ?>" class="quick-action-btn">
                <span class="dashicons dashicons-groups"></span>
                Manage Agents
            </a>
            <a href="<?php echo home_url(); ?>" target="_blank" class="quick-action-btn">
                <span class="dashicons dashicons-external"></span>
                View Site
            </a>
        </div>
    </div>

    <!-- Integrations Status -->
    <div class="ai-realty-card">
        <h2>🔌 Active Integrations</h2>
        <div class="integrations-list">
            <?php
            $integrations = array(
                'elementor/elementor.php' => array('name' => 'Elementor', 'icon' => 'dashicons-editor-table'),
                'contact-form-7/wp-contact-form-7.php' => array('name' => 'Contact Form 7', 'icon' => 'dashicons-email'),
                'seo-by-rank-math/rank-math.php' => array('name' => 'Rank Math SEO', 'icon' => 'dashicons-chart-line'),
                'wpforms-lite/wpforms.php' => array('name' => 'WPForms', 'icon' => 'dashicons-feedback'),
                'optima-express/optima-express.php' => array('name' => 'iHomeFinder IDX', 'icon' => 'dashicons-building'),
            );

            foreach ($integrations as $plugin => $data) {
                $is_active = is_plugin_active($plugin);
                $status_class = $is_active ? 'active' : 'inactive';
                $status_text = $is_active ? 'Active' : 'Not Installed';
                $status_icon = $is_active ? 'dashicons-yes' : 'dashicons-minus';

                echo '<div class="integration-item ' . $status_class . '">';
                echo '<span class="dashicons ' . $data['icon'] . '"></span>';
                echo '<span class="integration-name">' . $data['name'] . '</span>';
                echo '<span class="integration-status"><span class="dashicons ' . $status_icon . '"></span> ' . $status_text . '</span>';
                echo '</div>';
            }

            // GoHighLevel
            $ghl_api_key = get_option('ai_realty_ghl_api_key', '');
            $ghl_active = !empty($ghl_api_key);
            echo '<div class="integration-item ' . ($ghl_active ? 'active' : 'inactive') . '">';
            echo '<span class="dashicons dashicons-cloud"></span>';
            echo '<span class="integration-name">GoHighLevel</span>';
            echo '<span class="integration-status"><span class="dashicons ' . ($ghl_active ? 'dashicons-yes' : 'dashicons-minus') . '"></span> ' . ($ghl_active ? 'Configured' : 'Not Configured') . '</span>';
            echo '</div>';
            ?>
        </div>
    </div>

    <!-- MCP Information -->
    <div class="ai-realty-card">
        <h2>🤖 Claude MCP Integration</h2>
        <p>This plugin exposes a Model Context Protocol (MCP) API that allows Claude AI to interact with your WordPress site.</p>

        <div style="background: #f0f0f1; padding: 15px; border-left: 4px solid #2271b1; margin-top: 10px;">
            <h4>API Endpoint:</h4>
            <code style="display: block; padding: 10px; background: white; margin-top: 5px;">
                <?php echo rest_url('ai-builder/v1/'); ?>
            </code>

            <h4 style="margin-top: 15px;">Available Commands:</h4>
            <ul style="margin-left: 20px;">
                <li><code>/build-site</code> - Build entire site from prompt</li>
                <li><code>/create-page</code> - Create new page</li>
                <li><code>/update-page</code> - Update existing page</li>
                <li><code>/create-agent</code> - Add new agent</li>
                <li><code>/sync-leads</code> - Sync leads to GoHighLevel</li>
                <li><code>/status</code> - Get site status</li>
            </ul>
        </div>
    </div>
</div>

<style>
.ai-realty-dashboard {
    max-width: 1200px;
}

.ai-realty-header {
    margin-bottom: 30px;
}

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
    font-size: 20px;
}

.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 4px;
    font-weight: 500;
}

.status-indicator .dashicons {
    font-size: 20px;
    width: 20px;
    height: 20px;
}

.status-not_started {
    background: #f0f0f1;
    color: #50575e;
}

.status-building {
    background: #fcf9e8;
    color: #996800;
}

.status-completed {
    background: #d5f5d5;
    color: #007017;
}

.status-error {
    background: #fbe4e4;
    color: #cc1818;
}

.ai-realty-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
}

.stat-card {
    background: white;
    border: 1px solid #ccd0d4;
    border-radius: 4px;
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 15px;
    box-shadow: 0 1px 1px rgba(0,0,0,.04);
}

.stat-icon {
    font-size: 32px;
    color: #2271b1;
}

.stat-icon .dashicons {
    width: 32px;
    height: 32px;
    font-size: 32px;
}

.stat-content h3 {
    margin: 0;
    font-size: 32px;
    font-weight: 600;
    color: #1d2327;
}

.stat-content p {
    margin: 0;
    color: #646970;
}

.quick-actions {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 15px;
}

.quick-action-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 15px 20px;
    background: #f6f7f7;
    border: 1px solid #dcdcde;
    border-radius: 4px;
    text-decoration: none;
    color: #2c3338;
    transition: all 0.2s;
}

.quick-action-btn:hover {
    background: #2271b1;
    color: white;
    border-color: #2271b1;
}

.integrations-list {
    display: grid;
    gap: 10px;
}

.integration-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px;
    background: #f6f7f7;
    border-radius: 4px;
    border-left: 4px solid #dcdcde;
}

.integration-item.active {
    border-left-color: #00a32a;
    background: #f0f6fc;
}

.integration-item .dashicons {
    font-size: 20px;
    width: 20px;
    height: 20px;
}

.integration-name {
    flex: 1;
    font-weight: 500;
}

.integration-status {
    display: flex;
    align-items: center;
    gap: 4px;
    color: #646970;
    font-size: 13px;
}

.progress-bar {
    width: 100%;
    height: 30px;
    background: #f0f0f1;
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #2271b1, #72aee6);
    animation: progress 2s infinite;
}

@keyframes progress {
    0% { width: 0%; }
    50% { width: 70%; }
    100% { width: 100%; }
}

.progress-message {
    margin-top: 10px;
    font-weight: 500;
    color: #2271b1;
}
</style>

<script>
jQuery(document).ready(function($) {
    $('#ai-realty-build-btn, #ai-realty-rebuild-btn').on('click', function() {
        var prompt = $('#ai-realty-prompt').val();

        $('#ai-realty-build-progress').show();
        $('#ai-realty-build-log').hide();
        $(this).prop('disabled', true);

        $.ajax({
            url: aiRealtyAutogen.rest_url + 'build-site',
            method: 'POST',
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-WP-Nonce', aiRealtyAutogen.rest_nonce);
            },
            data: JSON.stringify({ prompt: prompt }),
            contentType: 'application/json',
            success: function(response) {
                $('#ai-realty-build-progress').hide();
                $('#ai-realty-build-btn, #ai-realty-rebuild-btn').prop('disabled', false);

                if (response.success) {
                    alert('Site built successfully! Refreshing page...');
                    location.reload();
                } else {
                    alert('Build failed: ' + response.message);
                }

                // Show log
                if (response.log && response.log.length > 0) {
                    var logHtml = '';
                    response.log.forEach(function(entry) {
                        logHtml += entry.time + ': ' + entry.message + '\n';
                    });
                    $('.build-log-content').text(logHtml);
                    $('#ai-realty-build-log').show();
                }
            },
            error: function(xhr) {
                $('#ai-realty-build-progress').hide();
                $('#ai-realty-build-btn, #ai-realty-rebuild-btn').prop('disabled', false);
                alert('Error: ' + xhr.responseText);
            }
        });
    });
});
</script>
