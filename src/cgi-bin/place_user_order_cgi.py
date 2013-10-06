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
tray = '4622236/1,4622238+4622296/1,+4622370/1'#args["tray"].value
tip = '5'#args["tip"].value
first_name = 'Example'#args["first_name"].value
last_name = 'User'#args["last_name"].value
email = 'testing@ordrin.com'#args["email"].value
current_pw = 'password'#args["current_pw"].value
phone = None
addr = None
addr2 = None
city = None
state = None
nick = 'Work'#args["nick"].value
card_name = None
card_number = None
card_cvc = None
card_expiry = None
card_bill_addr = None
card_bill_addr2 = None
card_bill_state = None
card_bill_zip = None
card_bill_phone = None
card_nick = 'Work'#args["card_nick"].value
delivery_date = 'ASAP'#args["delivery_date"].value
delivery_time = None

try:
  x = ordrin_api.ordrin_api.order_user(rid,tray, tip, first_name,
    last_name, email, current_pw, phone, addr, addr2,
    city, state, nick, card_name, card_number, card_cvc,
    card_expiry, card_bill_addr, card_bill_addr2, card_bill_state,
    card_bill_zip, card_bill_phone, card_nick, delivery_date,
    delivery_time)


  print "Content-type:application/json"
  print
  print x

except:
  print '''HTTP/1.1 401 Unauthorized 
Content-type:application/json'''
  print
  print "{}"
