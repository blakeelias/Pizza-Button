define(["api/newCreditCard"],
    function(newCreditCard) {
        return function() {        
            var o_inputData = {
                s_firstName:    document.forms["account-form"].firstName.value,
                s_lastName:     document.forms["account-form"].lastName.value,
                s_email:        document.forms["account-form"].email.value,
                s_number:       document.forms["account-form"].number.value,
                s_password1:    document.forms["account-form"].password1.value,
                s_password2:    document.forms["account-form"].password2.value,
                s_deliveryAddress1: document.forms["account-form"].deliveryAddress1.value,
                s_deliveryAddress2: document.forms["account-form"].deliveryAddress2.value,
                s_deliveryCity: document.forms["account-form"].deliveryCity.value,
                s_deliveryState: document.forms["account-form"].deliveryState.value,
                s_deliveryZipCode: document.forms["account-form"].deliveryZipCode.value,
                s_creditCardNumber: document.forms["account-form"].creditCardNumber.value,
                s_creditCardCvc:    document.forms["account-form"].creditCardCvc.value,
                b_addressesAreSame: document.forms["account-form"].addressesAreSame.value,
                s_billingAddress1:  document.forms["account-form"].billingAddress1.value,
                s_billingAddress2:  document.forms["account-form"].billingAddress2.value,
                s_billingCity: document.forms["account-form"].billingCity.value,
                s_billingState: document.forms["account-form"].billingState.value,
                s_billingZipCode: document.forms["account-form"].billingZipCode.value
            };

            if(!o_inputData.s_number.match(/^1?[0-9]{10}$/)) {
                error("Please input phone number as XXXXXXXXXX.");
                return;
            }
            if(!o_inputData.s_email.match(/^.+\@.+\..+$/)) {
                error("Please input a valid email address.");
                return;
            }
            if(o_inputData.s_password1 != o_inputData.s_password2) {
                error("Passwords do not match.");
                return;
            }

            var ajaxData = {
                email : o_inputData.s_email,
                first_name : o_inputData.s_firstName,
                last_name : o_inputData.s_lastName,
                pw : CryptoJS.SHA1(o_inputData.s_password1).toString()
            }

            $.ajax("/cgi-bin/create_account_cgi.py", {
                type:           "GET",
                data:           ajaxData,
                contentType:    "application/json;charset=utf-8",
                success:        function(jqXHR) {
                    var data = (typeof jqXHR === "string") ?
                        jqXHR : JSON.parse(jqXHR);
                    clearError();
                    newCreditCard(o_inputData);
                },
                error:          function(jqXHR, textStatus, errorThrown) {
                    error("Encounted unexpected error: " +
                        textStatus + " " + errorThrown);
                }
            });
        }
    });

