#!/usr/bin/env python
import sys

import json
import requests.exceptions

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

rid = args["rid"].value
email = args["email"].value
tray = args["tray"].value
tip = args["tip"].value
first_name = args["first_name"].value
last_name = args["last_name"].value
phone = args["phone"].value
zipcode = args["zip"].value
addr = args["addr"].value
addr2 = None #args["addr2"].value
city = args["city"].value
state = args["state"].value
card_name = args["card_name"].value
card_number = args["card_number"].value
card_cvc =  args["card.cvc"].value
card_expiry =  args["card_expiry"].value
card_bill_addr = args["card_bill_addr"].value
card_bill_addr2 = None #args["card_bill_addr2"].value
card_bill_city = args["card_bill_city"].value
card_bill_state = args["card_bill_state"].value
card_bill_zip = args["card_bill_zip"].value
card_bill_phone = args["card_bill_phone"].value
delivery_date = args["delivery_date"].value
delivery_time = None

try: 
  x = ordrin_api.ordrin_api.order_guest(rid,email, tray, tip,
    first_name,last_name, phone, zipcode, addr,
    city, state, card_number, card_cvc,
    card_expiry, card_bill_addr,card_bill_city,
    card_bill_state, card_bill_zip, card_bill_phone, addr2,
    card_name, card_bill_addr2, 
    delivery_date, delivery_time)

  print "Content-type:application/json"
  print
  print x

except:
  print '''HTTP/1.1 401 Unauthorized 
Content-type:application/json'''
  print
  print "{}"

