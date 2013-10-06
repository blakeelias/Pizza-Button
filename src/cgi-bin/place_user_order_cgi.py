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

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.

rid = args["rid"].value
tip = args["tip"].value
first_name = args["first_name"].value
last_name = args["last_name"].value
email = args["email"].value
current_pw = args["current_pw"].value
nick = args["nick"].value
card_nick = args["card_nick"].value
delivery_date = args["delivery_date"].value

return  ordrin_api.ordrin_api.order_user(rid, tip, first_name,
    last_name, email, current_pw, nick, card_nick,
    delivery_date)


