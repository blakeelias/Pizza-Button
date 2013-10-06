/**
 * Uses JQuery to set up tabs for account and order
 * information.
 **/

define(["frontend/setUpRestaurantsTable"],
    function(setUpRestTable) {
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
                },
                activate: function(event, ui) {
                    var active = $("#dropdown").tabs("option", "active");
                    if (active == 1) {
                        setUpRestTable();
                    }
                }
                
            }).css("visibility","visible");
        }
    });
