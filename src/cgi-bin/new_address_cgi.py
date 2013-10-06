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
  "nick" = __,
  "phone" = __,
  "zip" = __,
  "addr" = __,
  "addr2" = __, default None
  "city" = __,
  "state" = __,
  "current_pw" = __,
}
'''

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.

email = args["email"].value
nick = args["nick"].value
zipcode= args["zip"].value
phone = args["phone"].value
addr = args["addr"].value
city = args["city"].value
state = args["state"].value
current_pw = args["current_pw"].value

try:
  x = ordrin_api.ordrin_api.create_addr(email, nick, phone,zipcode, addr, city, state, current_pw)
  print "Content-type:application/json"
  print
  print json.dumps(x)
except HTTPError as e:
  print '''HTTP/1.1 404 Client 
Content-type:application/json'''
  print
  print "{}"
   

