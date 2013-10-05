/**
 * Uses JQuery to set up tabs for account and order
 * information.
 **/

define([],
    function() {
        $("#dropdown").tabs({
            active:     1,
            collapsible: true,
            heightStyle: "content",
            hide: {
                effect: "slide"
            }
            
        });
    });
