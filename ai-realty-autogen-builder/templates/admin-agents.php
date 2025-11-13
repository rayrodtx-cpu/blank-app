<?php
/**
 * Admin Agents Template
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

global $wpdb;
$agents_table = $wpdb->prefix . 'ai_realty_agents';
$agents = $wpdb->get_results("SELECT * FROM $agents_table ORDER BY created_at DESC");
$total_agents = count($agents);
?>

<div class="wrap ai-realty-agents">
    <h1><?php echo esc_html(get_admin_page_title()); ?></h1>

    <div class="ai-realty-header">
        <p class="description">
            Manage your real estate agents. Each agent gets a unique tracking link for lead attribution.
        </p>
    </div>

    <div class="ai-realty-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h2>👥 Agents (<?php echo $total_agents; ?> total)</h2>
            <button type="button" class="button button-primary" id="add-agent-btn">
                <span class="dashicons dashicons-plus"></span> Add New Agent
            </button>
        </div>

        <?php if ($total_agents > 0): ?>
            <table class="wp-list-table widefat fixed striped">
                <thead>
                    <tr>
                        <th>Agent ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Tracking Link</th>
                        <th>Date Added</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($agents as $agent): ?>
                        <tr>
                            <td><code><?php echo esc_html($agent->agent_id); ?></code></td>
                            <td><strong><?php echo esc_html($agent->name); ?></strong></td>
                            <td><?php echo esc_html($agent->email); ?></td>
                            <td><?php echo esc_html($agent->phone); ?></td>
                            <td>
                                <input type="text"
                                       value="<?php echo esc_url(home_url('?agent=' . $agent->agent_id)); ?>"
                                       readonly
                                       class="agent-link"
                                       style="width: 100%; max-width: 400px;">
                                <button type="button" class="button button-small copy-link-btn" data-link="<?php echo esc_url(home_url('?agent=' . $agent->agent_id)); ?>">
                                    Copy
                                </button>
                            </td>
                            <td><?php echo esc_html(date('M j, Y', strtotime($agent->created_at))); ?></td>
                        </tr>
                        <?php if ($agent->bio): ?>
                            <tr>
                                <td colspan="6" style="background: #f9f9f9; padding: 10px;">
                                    <strong>Bio:</strong> <?php echo esc_html($agent->bio); ?>
                                </td>
                            </tr>
                        <?php endif; ?>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php else: ?>
            <div class="notice notice-info">
                <p><strong>No agents yet!</strong> Add your first agent to start tracking leads.</p>
            </div>
        <?php endif; ?>
    </div>

    <!-- Add Agent Modal -->
    <div id="add-agent-modal" style="display: none;">
        <div class="modal-backdrop" id="modal-backdrop"></div>
        <div class="modal-content">
            <h2>Add New Agent</h2>
            <form id="add-agent-form">
                <table class="form-table">
                    <tr>
                        <th><label for="agent_id">Agent ID</label></th>
                        <td>
                            <input type="text" id="agent_id" name="agent_id" class="regular-text" placeholder="agent001" required>
                            <p class="description">Unique identifier for this agent</p>
                        </td>
                    </tr>
                    <tr>
                        <th><label for="agent_name">Name *</label></th>
                        <td><input type="text" id="agent_name" name="name" class="regular-text" required></td>
                    </tr>
                    <tr>
                        <th><label for="agent_email">Email *</label></th>
                        <td><input type="email" id="agent_email" name="email" class="regular-text" required></td>
                    </tr>
                    <tr>
                        <th><label for="agent_phone">Phone</label></th>
                        <td><input type="tel" id="agent_phone" name="phone" class="regular-text"></td>
                    </tr>
                    <tr>
                        <th><label for="agent_bio">Bio</label></th>
                        <td><textarea id="agent_bio" name="bio" class="large-text" rows="4"></textarea></td>
                    </tr>
                </table>

                <div style="text-align: right; margin-top: 20px;">
                    <button type="button" class="button" id="cancel-agent-btn">Cancel</button>
                    <button type="submit" class="button button-primary">Add Agent</button>
                </div>
            </form>
        </div>
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

.agent-link {
    font-family: monospace;
    font-size: 12px;
}

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
    z-index: 100000;
}

.modal-content {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    padding: 30px;
    border-radius: 4px;
    box-shadow: 0 5px 50px rgba(0, 0, 0, 0.3);
    z-index: 100001;
    max-width: 600px;
    width: 90%;
    max-height: 90vh;
    overflow-y: auto;
}

.modal-content h2 {
    margin-top: 0;
}
</style>

<script>
jQuery(document).ready(function($) {
    // Open modal
    $('#add-agent-btn').on('click', function() {
        $('#add-agent-modal').show();
    });

    // Close modal
    $('#cancel-agent-btn, #modal-backdrop').on('click', function() {
        $('#add-agent-modal').hide();
        $('#add-agent-form')[0].reset();
    });

    // Submit form
    $('#add-agent-form').on('submit', function(e) {
        e.preventDefault();

        var formData = {
            agent_id: $('#agent_id').val(),
            name: $('#agent_name').val(),
            email: $('#agent_email').val(),
            phone: $('#agent_phone').val(),
            bio: $('#agent_bio').val()
        };

        $.ajax({
            url: aiRealtyAutogen.rest_url + 'create-agent',
            method: 'POST',
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-WP-Nonce', aiRealtyAutogen.rest_nonce);
            },
            data: JSON.stringify(formData),
            contentType: 'application/json',
            success: function(response) {
                if (response.success) {
                    alert('Agent added successfully!');
                    location.reload();
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(xhr) {
                alert('Error adding agent: ' + xhr.responseText);
            }
        });
    });

    // Copy link
    $('.copy-link-btn').on('click', function() {
        var link = $(this).data('link');
        var temp = $('<input>');
        $('body').append(temp);
        temp.val(link).select();
        document.execCommand('copy');
        temp.remove();

        $(this).text('Copied!');
        setTimeout(() => {
            $(this).text('Copy');
        }, 2000);
    });
});
</script>
