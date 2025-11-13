<?php
/**
 * Fired during plugin deactivation.
 */
class AI_Realty_Autogen_Deactivator {

    /**
     * Deactivation tasks.
     */
    public static function deactivate() {
        // Flush rewrite rules
        flush_rewrite_rules();

        // Note: We don't delete options or tables on deactivation
        // This preserves user data if they reactivate
        // Use uninstall.php for complete data removal

        error_log('AI Realty Autogen Builder deactivated');
    }
}
