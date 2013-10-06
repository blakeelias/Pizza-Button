#!/usr/bin/env python
import sys

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

email = args["email"].value
current_pw = args["current_pw"].value

ordrin_api.ordrin_api.get_order_history(email,
    current_pw)


