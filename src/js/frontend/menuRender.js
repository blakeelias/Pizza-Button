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
                    $("#menu").html(jqXHR);
                    $("#menu").prepend("<a id='placeOrder'>Place order</a>");
                    var quantities = {};
                    $("#menu #placeOrder").click(function() {
                        alert('hi');
                        $('.quantity').each(function() {
                            //if ($(this).parentElement) {
                                quantities[$(this).parent().attr('id')] = $(this).val();
                                //alert('value: ' + $(this).val() + $(this).parentElement.attr('id'));
                            //}
                        });
                        
//                        document.getElementById();
                        alert(quantities);
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