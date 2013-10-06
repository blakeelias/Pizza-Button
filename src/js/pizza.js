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
	   'frontend/accountSubmit', 'frontend/loadConfirmation', 'frontend/hideConfirmation', 'frontend/pizzaButtonOnClick', 'frontend/menuRender'],
	  function(setUpTabs, displayBilling, accountSubmit, loadConfirmation, hideConfirmation, pizzaButtonOnClick, menuRender) {
        $(document).ready(function() {
            $("#addresses-are-same").click(displayBilling);
            setUpTabs();
            $("#account-submit").click(accountSubmit);
    	    $("#cancel-order").click(hideConfirmation);
    	    $("#confirmationContainer").on('click', hideConfirmation);
    	    $("#confirmationWindow").on('click', function(e) {e.stopPropagation();});
    	    //TODO (whaack): REMOVE, just here for testing
    	    $("#pizza-button").click(pizzaButtonOnClick);
    	    $("#ui-id-2").click(menuRender);
    	    
        });
    });