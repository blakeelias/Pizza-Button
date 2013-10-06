#!/usr/bin/env python
import sys

import cgi
import cgitb
from ordrin_api import ordrin_api
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

Returns a list of restaurants:
[
]
'''

deliveryList = ordrin_api.delivery_list("ASAP", args["addr"].value, args["city"].value, args["zip"].value)
pizzaRestaurants = filter(lambda restaurant: 'cu' in restaurant and 'Pizza' in restaurant['cu'], deliveryList)

print(json.dumps(pizzaRestaurants))