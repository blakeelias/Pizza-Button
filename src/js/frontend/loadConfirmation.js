define([],
    function() {
        return function(orderInfo) {
	    $("#confirmationContainer").css("display", "block");
	    var ajaxData = {
		email: accountInfo.username,
		current_pw: accountInfo.password
	    }
	    $("#confirm-order").click(
				      function () {
	    $.ajax("/cgi-bin/place_user_order_cgi.py", {
                    type:           "GET",
			data:           ajaxData,
			contentType:    "application/json;charset=utf-8",
			success:        function(jqXHR) {
			var data = jqXHR;
			loadConfirmation(data['tray']);
		    },
			error:          function(jqXHR, textStatus, errorThrown) {
			
		    }
		}); }
				      );


        }
    });
