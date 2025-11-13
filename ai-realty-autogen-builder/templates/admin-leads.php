<?php
/**
 * Admin Leads Template
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

$attribution = new AI_Realty_Agent_Attribution();
$leads = $attribution->get_all_leads(50, 0);
$total_leads = $attribution->get_leads_count();
?>

<div class="wrap ai-realty-leads">
    <h1><?php echo esc_html(get_admin_page_title()); ?></h1>

    <div class="ai-realty-header">
        <p class="description">
            All leads captured from contact forms, IDX inquiries, and other sources.
        </p>
    </div>

    <?php if ($total_leads > 0): ?>
        <div class="ai-realty-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h2>📧 Leads (<?php echo $total_leads; ?> total)</h2>
                <button type="button" class="button button-primary" id="sync-leads-btn">
                    <span class="dashicons dashicons-update"></span> Sync to GoHighLevel
                </button>
            </div>

            <table class="wp-list-table widefat fixed striped">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Agent ID</th>
                        <th>Source</th>
                        <th>GHL Synced</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($leads as $lead): ?>
                        <tr>
                            <td><strong><?php echo esc_html($lead->name); ?></strong></td>
                            <td><?php echo esc_html($lead->email); ?></td>
                            <td><?php echo esc_html($lead->phone); ?></td>
                            <td>
                                <?php if ($lead->agent_id): ?>
                                    <span class="badge"><?php echo esc_html($lead->agent_id); ?></span>
                                <?php else: ?>
                                    <span class="badge badge-gray">None</span>
                                <?php endif; ?>
                            </td>
                            <td><?php echo esc_html($lead->source); ?></td>
                            <td>
                                <?php if ($lead->ghl_synced): ?>
                                    <span class="dashicons dashicons-yes" style="color: green;"></span>
                                <?php else: ?>
                                    <span class="dashicons dashicons-minus" style="color: gray;"></span>
                                <?php endif; ?>
                            </td>
                            <td><?php echo esc_html(date('M j, Y g:i a', strtotime($lead->created_at))); ?></td>
                        </tr>
                        <?php if ($lead->message): ?>
                            <tr class="lead-message-row">
                                <td colspan="7" style="background: #f9f9f9; padding: 10px;">
                                    <strong>Message:</strong> <?php echo esc_html($lead->message); ?>
                                </td>
                            </tr>
                        <?php endif; ?>
                    <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    <?php else: ?>
        <div class="ai-realty-card">
            <div class="notice notice-info">
                <p><strong>No leads yet!</strong> Leads will appear here when visitors submit contact forms on your site.</p>
            </div>
        </div>
    <?php endif; ?>
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

.badge {
    display: inline-block;
    padding: 3px 8px;
    background: #2271b1;
    color: white;
    border-radius: 3px;
    font-size: 11px;
    font-weight: 500;
}

.badge-gray {
    background: #dcdcde;
    color: #50575e;
}

.lead-message-row {
    border-left: 4px solid #2271b1;
}
</style>

<script>
jQuery(document).ready(function($) {
    $('#sync-leads-btn').on('click', function() {
        var button = $(this);
        button.prop('disabled', true).html('<span class="dashicons dashicons-update"></span> Syncing...');

        $.ajax({
            url: aiRealtyAutogen.rest_url + 'sync-leads',
            method: 'POST',
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-WP-Nonce', aiRealtyAutogen.rest_nonce);
            },
            success: function(response) {
                button.prop('disabled', false).html('<span class="dashicons dashicons-update"></span> Sync to GoHighLevel');

                if (response.success) {
                    alert('Synced ' + response.synced + ' of ' + response.total + ' leads to GoHighLevel!');
                    location.reload();
                } else {
                    alert('Sync failed. Make sure GoHighLevel is configured in Settings.');
                }
            },
            error: function(xhr) {
                button.prop('disabled', false).html('<span class="dashicons dashicons-update"></span> Sync to GoHighLevel');
                alert('Error syncing leads: ' + xhr.responseText);
            }
        });
    });
});
</script>
