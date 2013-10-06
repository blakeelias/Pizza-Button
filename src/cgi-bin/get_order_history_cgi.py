#!/usr/bin/env python
import sys

import json
from requests.exceptions import HTTPError

import cgi
import cgitb


import ordrin_api

'''
Expects the following arguments:
args = {
  "email" = __,
  "current_pw" = __,
}
'''


args = cgi.FieldStorage()

# Call methods on args.

email = 'demitri@gmail.com'#args["email"].value
current_pw = '12345'#args["current_pw"].value

try:
  x = ordrin_api.ordrin_api.get_order_history(email,
    current_pw)
  if len(x) > 0:
    print "Content-type:application/json"
    print
    print json.dumps(x[-1])
  
  print "Content-type:application/json"
  print
  print "[]"
except HTTPError as e:
  print '''HTTP/1.1 404 Client 
Content-type:application/json'''
  print
  print "{}"
   
  


