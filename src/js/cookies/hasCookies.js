define([],
    function() {
        return function() {
            return $.cookie("pizza-username") != null && $.cookie("pizza-password") != null);
        }
    });
