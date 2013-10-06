define([],
    function() {
        return function() { 
            $(".billingAddress").css("display",
                (document.forms.account-form.addressesAreSame.checked) ? "none" : "inline");
        }
    });
