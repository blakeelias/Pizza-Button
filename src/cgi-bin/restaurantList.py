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

Returns a list of restaurants along with pagination info for data tables:
{
    iTotalRecords,
    iTotalDisplayRecords,
    sEcho,
    [
      [Name, Address, Minimum, Delivery Time],
      ...,
      ...
    ]
'''

iDisplayStart = args['iDisplayStart'].value
iDisplayLength = args['iDisplayLength'].value

# Prevent API call from printing a line that we don't want in the output
save_stdout = sys.stdout
sys.stdout = open('trash', 'w')
deliveryList = ordrin_api.delivery_list("ASAP", args["addr"].value, args["city"].value, args["zip"].value)
sys.stdout = save_stdout
pizzaRestaurants = filter(lambda restaurant: 'cu' in restaurant and 'Pizza' in restaurant['cu']
                                              and 'is_delivering' in restaurant and restaurant['is_delivering'] > 0,
                          deliveryList)
iTotalRecords = len(pizzaRestaurants)
pizzaRestaurants = pizzaRestaurants[int(iDisplayStart):int(iDisplayStart)+int(iDisplayLength)]
restaurantsArray = [[r['id'], r['na'], r['addr'], r['mino'], r['del']] for r in pizzaRestaurants]

answer = {
    'iTotalRecords': iTotalRecords,
    'iTotalDisplayRecords': len(pizzaRestaurants),
    'sEcho': args['sEcho'].value,
    'aaData': restaurantsArray
}

print(json.dumps(answer))