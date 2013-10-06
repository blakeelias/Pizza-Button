/**
 * Require JS loader for the pizza button app.
 **/

requirejs.config({
    baseUrl: 'js',
    paths: {
        api: "./api",
        cookies: "./cookies",
        frontend: "./frontend"
    }
});

requirejs(['frontend/tabs', 'frontend/displayBilling'],
    function(setUpTabs, displayBilling) {
        $("#addressesAreSame").onclick(displayBilling(document.forms.account-form.addressesAreSame.value);
        setUpTabs();
        
    });

        

