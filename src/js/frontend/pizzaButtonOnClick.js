define(['cookies/hasCookies', 'cookies/getCookies'],
       function(hasCookies, getCookies) {
        return function() {
	    if (hasCookies()) {
		var accountInfo = getCookies();
		var ajaxData = {
		    username: accountInfo.username,
		    password: accountInfo.password
		}
		$.ajax("/cgi-bin/get_account_info_cgi.py", {
		    type:           "GET",
		    data:           ajaxData,
		    contentType:    "application/json;charset=utf-8",
		    success:        function(jqXHR) {
                    var data = jqXHR;
                },
		    error:          function(jqXHR, textStatus, errorThrown) {
			    error("Encounted unexpected error while getting account info. Try creating a new account");
			}
		    });
	    }
	    else {
		error("Please login or create an account");
		$("#dropdown").tabs({active: 0});
		$('html, body').animate({
			scrollTop: $("#account-info-error").offset().top
			    }, 500);
	    }
        }
    });
