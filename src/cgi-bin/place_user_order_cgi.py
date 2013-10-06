#!/usr/bin/env python
import sys

import cgi
import cgitb


import ordrin_api

'''
Expects the following arguments:
args = {
  "rid" = __,
  "tip" = __,
  "first_name" = __,
  "last_name" = __,
  "email" = __,
  "current_pw" = __,
  "nick" = __,
  "card_nick" = __,
   
   EITHER
   "delivery_date" = __,
   "delivery_time" = __,

   OR

   "delivery_date" = __, (ASAP)
}
'''

args = cgi.FieldStorage()

# Call methods on args.

rid = '147'#args["rid"].value
tip = '5'#args["tip"].value
first_name = 'Example'#args["first_name"].value
last_name = 'User'#args["last_name"].value
email = 'testing@ordrin.com'#args["email"].value
current_pw = 'password'#args["current_pw"].value
nick = 'Work'#args["nick"].value
card_nick = 'Work'#args["card_nick"].value
delivery_date = 'ASAP'#args["delivery_date"].value

x = ordrin_api.ordrin_api.order_user(rid, tip, first_name,
    last_name, email, current_pw, nick, card_nick,
    delivery_date)

print "Content-type:application/json"
print
print x



