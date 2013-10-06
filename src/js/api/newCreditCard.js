define([],//'api/newAddress'],
    function(){//newAddress) {
        return function (data) {
            var o_nAddData = (typeof data === "string") ? data : JSON.parse(data);
        }
    });
