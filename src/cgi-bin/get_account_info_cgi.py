#!/usr/bin/env python
import sys
from requests.exceptions import HTTPError
import json
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

email = args["email"].value
current_pw = args["current_pw"].value

try:
  x =   ordrin_api.ordrin_api.get_account_info(email,
    current_pw)
  print "Content-type:application/json"
  print
  print json.dumps(x)
except:
  print '''HTTP/1.1 401 Unauthorized 
Content-type:application/json'''
  print
  print "{}"
   
