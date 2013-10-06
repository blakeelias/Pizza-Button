define(['createCookies'],
    function(createCookies) {
        return function (data) {
            var myData = (typeof data === "string") ? JSON.parse(data) : data;

            var username = myData.s_email;
            var password = myData.s_passwordHash;

            $.ajax('/cgi-bin/new_address_cgi.py',
                {
                    type: "GET",
                    data: {
                        email: myData.s_email,
                        nick: "address1",
                        zipcode: myData.s_deliveryZipCode,
                        phone: myData.s_number,
                        addr: myData.s_deliveryAddress1,
                        addr2: myData.s_deliveryAddress2,
                        city: myData.s_deliveryCity,
                        state: myData.s_deliveryState,
                        current_pw: myData.s_passwordHash
                    },
                    contentType: "application/json;charset:utf-8",
                    success: function(jqXHR) {
                        createCookies(username, password);
                        $("#dropdown").tabs({
                            active: false
                        });
                    },
                    error: function(jqXHR, textStatus, errorThrown) {
                        error("Encountered unexpected error while storing delivery address: " + textStatus + errorThrown);
                    }
                });
        };
    });

