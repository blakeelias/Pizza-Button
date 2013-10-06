define([],
    function() {
        return function() {
            return {
                username : $.cookie("pizza-username"),
                password : $.cookie("pizza-password")
            };
        }
    });
