define([],
    function() {
        //alert('in menuRender.js before inner function');
        
        return function() {
            
            var ajaxData = {
                rid : '28139'
            };
            //alert("in menuRender.js inner function");
            $.ajax("/cgi-bin/restaurantMenu.py", {
                type:           "GET",
                data:           ajaxData,
                contentType:    "text/html;charset=utf-8",
                success:        function(jqXHR) {
                    $("#order").html(jqXHR);
                    $("#order").prepend("<a id='placeOrder'>Place order</a>");
                    $("#order #placeOrder").click(function() {
                        alert('hi');
                        $('input#quantity').each(function() {
                            //if ($(this).parentElement) {
                                alert('value: ' + $(this).val() + $(this).parentElement.attr('id'));
                            //}
                        });
                    });
                },
                error:          function(jqXHR, textStatus, errorThrown) {
                    error("Encounted unexpected error while creating account.  The email address may already be in use: " +
                        textStatus + " " + errorThrown);
                }
            });
            
        }
    }
);