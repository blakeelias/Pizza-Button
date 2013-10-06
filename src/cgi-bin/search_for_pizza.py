#!/usr/bin/env python
import sys

import cgi
import cgitb
import ordrin_api
import json

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.

'''
Expects the following arguments: 
{
    'addr': __,
    'city': __,
    'zip': __,
}

Returns the following shit:
{
    returns a fucking pizza
}
'''

deliveryList = ordrin_api.delivery_list("ASAP", args["addr"].value, args["city"].value, args["zip"].value)
pizzaRestaurants = filter(lambda restaurant: 'cu' in restaurant and 'Pizza' in restaurant['cu'], deliveryList)

print(json.dumps(pizzaRestaurants))
