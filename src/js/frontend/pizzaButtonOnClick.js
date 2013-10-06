define(['cookies/hasCookies', 'cookies/getCookies', 'frontend/loadConfirmation'],
       function(hasCookies, getCookies, loadConfirmation) {
	var accountNotMade = function() {
		error("Please login or create an account");
		$("#dropdown").tabs({active: 0});
		$('html, body').animate({
			scrollTop: $("#account-info-error").offset().top
			    }, 500);
	};
        return function() {
	    if (hasCookies()) {
		var accountInfo = getCookies();
		var ajaxData = {
		    email: accountInfo.username,
		    current_pw: accountInfo.password
		}
		$.ajax("/cgi-bin/get_account_info_cgi.py", {
		    type:           "GET",
		    data:           ajaxData,
		    contentType:    "application/json;charset=utf-8",
		    success:        function(jqXHR) {
                    var data = jqXHR;
		    // TODO (whaack): Handle no past orders
		    loadConfirmation(data);
                },
		    error:          function(jqXHR, textStatus, errorThrown) {
			    accountNotMade();
			}
		    });
	    }
	    else {
		accountNotMade();
	    }
        }
    });
