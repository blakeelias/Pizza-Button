define(['api/newAddress'],
    function(newAddress) {
        return function (data) {
            var myData = (typeof data === "string") ? JSON.parse(data) : data;

            $.ajax("/cgi-bin/new_credit_card_cgi.py",
                    {
                        type: "GET",
                        data: {
                            email: myData.s_Email,
                            card_nick: "creditcard1",
                            card_cvc: myData.s_creditCardCvc,
                            card_expiry:myData.s_creditCardExp,
                            bill_addr:myData.s_billingAddress1,
                            bill_addr2:myData.s_billingAddress2,
                            bill_city:myData.s_billingCity,
                            bill_state:myData.s_billingState,
                            bill_zip:myData.s_billingZipCode,
                            bill_phone:myData.s_number,
                            current_pw:myData.s_passwordHash
                        },
                        contentType: "application/json",
                        success: function(jqXHR) {
                            newAddress(myData);
                        },
                        error: function (jqXHR, textStatus, errorThrown) {
                            error("Encountered unexpected error while processing credit card information: " + textStatus + " " + errorThrown);
                        }
                    });


        };
    });
