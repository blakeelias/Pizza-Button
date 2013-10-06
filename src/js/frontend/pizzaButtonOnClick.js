define(['cookies/hasCookies', 'cookies/getCookies'],
       function(hasCookies, getCookies) {
        return function() {
	    if (hasCookies()) {
		//make an order
	    }
	    else {
		error("Please login or create an account");
		$("#dropdown").tabs({active: 0});
	    }
        }
    });
