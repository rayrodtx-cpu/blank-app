(function($) {
    'use strict';

    /**
     * AI Realty Autogen - Public JavaScript
     * Handles agent cookie tracking and form field injection
     */

    $(document).ready(function() {

        // Check for agent parameter in URL and set cookie
        const urlParams = new URLSearchParams(window.location.search);
        const agentParam = urlParams.get('agent');

        if (agentParam) {
            setAgentCookie(agentParam);
        }

        // Get current agent from cookie
        const currentAgent = getAgentCookie();

        if (currentAgent) {
            console.log('AI Realty: Agent tracking active -', currentAgent);
            injectAgentIdIntoForms(currentAgent);
        }

        /**
         * Set agent cookie
         */
        function setAgentCookie(agentId) {
            const cookieName = aiRealtyPublic.cookie_name || 'agent_ref';
            const expiryDays = parseInt(aiRealtyPublic.cookie_expiry) || 30;
            const date = new Date();
            date.setTime(date.getTime() + (expiryDays * 24 * 60 * 60 * 1000));
            const expires = "expires=" + date.toUTCString();
            document.cookie = cookieName + "=" + agentId + ";" + expires + ";path=/";
            console.log('AI Realty: Agent cookie set -', agentId);
        }

        /**
         * Get agent cookie
         */
        function getAgentCookie() {
            const cookieName = aiRealtyPublic.cookie_name || 'agent_ref';
            const name = cookieName + "=";
            const decodedCookie = decodeURIComponent(document.cookie);
            const ca = decodedCookie.split(';');

            for (let i = 0; i < ca.length; i++) {
                let c = ca[i];
                while (c.charAt(0) === ' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) === 0) {
                    return c.substring(name.length, c.length);
                }
            }
            return null;
        }

        /**
         * Inject agent ID into all forms
         */
        function injectAgentIdIntoForms(agentId) {
            // Contact Form 7
            $('form.wpcf7-form').each(function() {
                if (!$(this).find('input[name="agent-id"]').length) {
                    $(this).append('<input type="hidden" name="agent-id" value="' + agentId + '" />');
                }
            });

            // WPForms
            $('form.wpforms-form').each(function() {
                if (!$(this).find('input[name="agent_id"]').length) {
                    $(this).append('<input type="hidden" name="agent_id" value="' + agentId + '" />');
                }
            });

            // iHomeFinder forms (retry after delay to ensure forms are loaded)
            setTimeout(function() {
                $('form[id^="ihf"]').each(function() {
                    if (!$(this).find('input[name="agent_id"]').length) {
                        $(this).append('<input type="hidden" name="agent_id" value="' + agentId + '" />');
                    }
                });
            }, 1000);

            // Generic forms
            $('form').not('.wpcf7-form, .wpforms-form, [id^="ihf"]').each(function() {
                // Only add to forms with email fields (likely contact forms)
                if ($(this).find('input[type="email"]').length && !$(this).find('input[name="agent_id"]').length) {
                    $(this).append('<input type="hidden" name="agent_id" value="' + agentId + '" />');
                }
            });

            console.log('AI Realty: Agent ID injected into forms');
        }

        // Re-inject on AJAX form loads (for dynamic forms)
        $(document).on('ajaxComplete', function() {
            const currentAgent = getAgentCookie();
            if (currentAgent) {
                setTimeout(function() {
                    injectAgentIdIntoForms(currentAgent);
                }, 500);
            }
        });

        // Listen for Contact Form 7 submissions
        $(document).on('wpcf7submit', function(event) {
            console.log('AI Realty: Contact Form 7 submission detected');
        });

        // Listen for WPForms submissions
        $(document).on('wpformsAjaxSubmitSuccess', function(event) {
            console.log('AI Realty: WPForms submission detected');
        });
    });

})(jQuery);
