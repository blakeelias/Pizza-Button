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

rid = '147'#args["rid"].value
email = 'testing@ordrin.com'#args["email"].value
tray ='4622236/1,4622238+4622296/1,+4622370/1' #args["tray"].value
tip = '5.05'#args["tip"].value
first_name = 'Example'#args["first_name"].value
last_name = 'User'#args["last_name"].value
phone = '2345678901'#args["phone"].value
zipcode = '77840'#args["zip"].value
addr = '1 Main Street'#args["addr"].value
addr2 = None#args["addr2"].value
city = 'College Station'#args["city"].value
state = 'TX'#args["state"].value
card_name ='Example User'# args["card_name"].value
card_number = '4111111111111111'#args["card_number"].value
card_cvc = '123'#args["card.cvc"].value
card_expiry = '02/2016'#args["card_expiry"].value
card_bill_addr = '1 Main Street'#args["card_bill_addr"].value
card_bill_addr2 = None#args["card_bill_addr2"].value
card_bill_city = 'College Station'#args["card_bill_city"].value
card_bill_state = 'TX'#args["card_bill_state"].value
card_bill_zip = '77840'#args["card_bill_zip"].value
card_bill_phone = '2345678901'#args["card_bill_phone"].value
delivery_date = 'ASAP' #args["delivery_date"].value
delivery_time = None

#try: 
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

#except:
 # print '''HTTP/1.1 401 Unauthorized 
#Content-type:application/json'''
 # print
  #print "{}"

