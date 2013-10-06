/**
 * Uses JQuery to set up tabs for account and order
 * information.
 **/

define([],
    function() {
        return function() {
            $("#dropdown").tabs({
                active: false,
                collapsible: true,
                heightStyle: "content",
                hide: {
                    effect: "slideUp"
                },
                show: {
                    effect: "slideDown"
                }
                
            }).css("visibility","visible");
        }
    });
