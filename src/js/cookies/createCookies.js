define([],
    function() {
        return function(username, password) {
            var date = new Date();
            date.setTime(date.getTime() + (14 * 24 * 60 * 60 * 1000));
            $.cookie("pizza-username",username, {expires : date});
            $.cookie("pizza-password",password, {expires : date});
        }
    });
