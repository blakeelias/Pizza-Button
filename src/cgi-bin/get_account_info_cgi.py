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

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.

email = 'demitri@gmail.com'#args["email"].value
current_pw = '12345666666666666'#args["current_pw"].value

try:
  x =   ordrin_api.ordrin_api.get_account_info(email,
    current_pw)
  print "Content-type:application/json"
  print
  print json.dumps(x)
except HTTPError as e:
  print '''HTTP/1.1 401 Unauthorized 
Content-type:application/json'''
  print
  print "{}"
   
