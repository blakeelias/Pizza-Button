define([],
    function() {
        return function () {
            var loadTable = function(data) {
                var myData = (typeof data === "string") ? JSON.parse(data) : data;

                $("#restaurants-table").dataTable({
                    "bProcessing":true,
                    "bServerSide":true,
                    "sAjaxSource":"/cgi-bin/restaurantList.py?addr="+data.addr+"&city="+data.city+"&zip="+data.zip,
                    "bSort": true,
                    "aoColumns": [
                        {"bVisible":false},
                        null,
                        {"bVisible":false},
                        null,
                        null
                    ]
                });
            };

            var mData = {addr: "3 Ames Street",city:"Cambridge",zip:"02142"};
            loadTable(mData);
        }


    });
