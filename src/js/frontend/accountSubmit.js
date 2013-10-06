define(["frontend/newCreditCard", "frontend/newAddress",
        "frontend/getOrder"],
    function(newCreditCard, newAddress, getOrder) {
        
        var b_newCreditCard = false;
        var b_newAddress = false;
        var o_inputData = {
            s_firstName:    document.forms.account-form.
            s_lastName:     document.forms.account-form.
            s_email:        document.forms.account-form.email,
            s_number:       document.forms.account-form.number,




        };

        if(s_number.match(/^1?[0-9]{10}$/)) 

        $.ajax({
            url:            "/cgi-bin/create_account_cgi.py",
            type:           "GET",
            contentType:    "application/json;charset=utf-8",
            success:        function(jqXHR) {
                var data = (typeof jqXHR === "string") ?
                    jqXHR : JSON.parse(jqXHR);
                if (b_newCreditCard) {
                    newCreditCard(o_inputData);
                } else if (b_newAddress) {
                    newAddress(o_inputData);
                } else {
                    getOrder();
                }
            }
        }
    });

