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
	   'frontend/accountSubmit', 'frontend/loadConfirmation'],
	  function(setUpTabs, displayBilling, accountSubmit, loadConfirmation) {
        $(document).ready(function() {
            $("#addresses-are-same").click(displayBilling);
            setUpTabs();
            $("#account-submit").click(accountSubmit);
	    //TODO (whaack): REMOVE, just here for testing
	    $("#pizza-button").click(loadConfirmation);
        });
    });

        

