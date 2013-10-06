define([],
    function() {
        return function() { 
            if ($("#addresses-are-same").prop("checked")) {
                $(".billingAddress").hide();
            } else {
                $(".billingAddress").show();
            }   
        }
    });
