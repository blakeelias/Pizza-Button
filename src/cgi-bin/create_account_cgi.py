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
  "pw" = __,
  "first_name" = __,
  "last_name" = __,
}
'''


args = cgi.FieldStorage()

# Call methods on args.
email = args["email"].value
pw = args["pw"].value
first_name = args['first_name'].value
last_name = args['last_name'].value

try:
  x = ordrin_api.ordrin_api.create_account(email, pw, first_name, last_name)
  print "Content-type:application/json"
  print
  print json.dumps(x) 

except HTTPError as e:
  print '''HTTP/1.1 401 Unauthorized 
Content-type:application/json'''
  print
  print "{}"

