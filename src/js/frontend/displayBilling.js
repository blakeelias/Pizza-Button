define([],
    function() {
        return function(hide) { 
            $(".billingAddress").css("display",
                (hide) ? "none" : "inline");
        }
    });
