/**
 * Require JS loader for the pizza button app.
 **/

clearError = function() {
    $(".error").empty();
}
error = function(errorThrown) {
    if (errorThrown == null) {
        return;
    } else if (typeof errorThrown === "string") {
        $(".error").html(errorThrown);
    } else if (errorThrown.hasOwnProperty("message")) {
        $(".error").html(errorThrown.message);
    }
}

requirejs.config({
    baseUrl: 'js',
    paths: {
        api: "./api",
        cookies: "./cookies",
        frontend: "./frontend"
    }
});

requirejs(['frontend/tabs', 'frontend/displayBilling', 
    'frontend/accountSubmit'],
    function(setUpTabs, displayBilling, accountSubmit) {
        $(document).ready(function() {
            $("#addressesAreSame").click(displayBilling);
            setUpTabs();
            $("#account-submit").click(accountSubmit);
        });
    });

        

