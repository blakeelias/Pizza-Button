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
	   'frontend/accountSubmit', 'frontend/loadConfirmation', 'frontend/hideConfirmation'],
	  function(setUpTabs, displayBilling, accountSubmit, loadConfirmation, hideConfirmation) {
        $(document).ready(function() {
            $("#addressesAreSame").click(displayBilling);
            setUpTabs();
            $("#account-submit").click(accountSubmit);
	    $("#cancel-order").click(hideConfirmation);
	    $("#confirmationContainer").click(hideConfirmation);
	    $("#confirmationWindow").click(function() {alert('yo');});
	    //TODO (whaack): REMOVE, just here for testing
	    $("#pizza-button").click(loadConfirmation);
        });
    });

        

