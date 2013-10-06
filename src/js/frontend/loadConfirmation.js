define(['frontend/hideConfirmation'],
    function(hideConfirmation) {
        return function(orderInfo) {
	    $("#confirmationContainer").css("display", "block");
	    var ajaxData = {
		email: orderInfo.username,
		current_pw: orderInfo.password
		//complete the order info object
	    }
	    $("#confirm-order").click(
				      function () {
	    $.ajax("/cgi-bin/place_user_order_cgi.py", {
                    type:           "GET",
			data:           ajaxData,
			contentType:    "application/json;charset=utf-8",
			success:        function(jqXHR) {
			//TODO(whaack): Say your order has been placed.
			hideConfirmation();
			
		    },
			error:          function(jqXHR, textStatus, errorThrown) {
			//Handle error of order not going through.
			hideConfirmation();
		    }
		}); }
				      );


        }
    });
