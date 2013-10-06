define(["cookies/getCookies", "cookies/hasCookies"],
    function(getCookies, hasCookies) {
        return function () {
            var loadTable = function(data) {
                var myData = (typeof data === "string") ? JSON.parse(data) : data;

                $("#restaurants-table").dataTable({
                    "bProcessing":true,
                    "bServerSide":true,
                    "sAjaxSource":"/cgi-bin/restaurantList.py?addr="+data.addr+"&city="+data.city+"&zip="+data.zip,
                    "bSort": true,
                    "bDestroy": true,
                    "iDisplayLength":5,
                    "aoColumns": [
                        {"bVisible":false},
                        null,
                        {"bVisible":false},
                        null,
                        null
                    ]
                });
            };

            var cookiesPresent = hasCookies();
            if(!cookiesPresent) {
                $("#dropdown").tabs({active : 0});
                error("Please create an account before setting order details.");
            }

            var cookieInfo = getCookies();
            var username = cookieInfo.username;
            var password = cookieInfo.password;

            $.ajax("/cgi-bin/single_address_cgi.py",
                    {
                        type : "GET",
                        data : {
                            email : username,
                            current_pw : password,
                            nick : "address1"
                        },
                        contentType : "application/json;charset:utf-8",
                        success : function(jqXHR) {
                            var o_jqXHR = (typeof jqXHR === "string") ? JSON.parse(jqXHR) : jqXHR;
                            loadTable(o_jqXHR);
                        },
                        error : function(jqXHR, textStatus, errorThrown) {
                            $("#dropdown").tabs({active : 0});
                            error("Please create an account before setting order details.");
                        }
                    });
        }


    });
