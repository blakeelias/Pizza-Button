define([],
    function() {
        return function(username, password) {
            $.cookie("pizza-username",username);
            $.cookie("pizza-password",password);
        }
    });
