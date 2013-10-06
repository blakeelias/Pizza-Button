#!/usr/bin/env python
import sys

import cgi
import cgitb


import ordrin_api

'''
Expects the following arguments:
args = {
  "email" = __,
  "nick" = __, default None
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
zipcode = args["zip"].value
phone = args["phone"].value
addr = args["addr"].value
addr2 = args["addr2"].value
city = args["city"].value
state = args["state"].value
current_pw = args["current_pw"].value

ordrin_api.ordrin_api.create_addr(email, nick, zipcode, phone,
    addr, addr2, city, state, current_pw)
