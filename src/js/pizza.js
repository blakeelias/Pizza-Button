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

requirejs(['frontend/tabs'],
    function(setUpTabs) {
        setUpTabs();
        
    });

        

