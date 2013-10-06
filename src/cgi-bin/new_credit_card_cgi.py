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
  "card_nick" = __,
  "card_number" = __,
  "card_cvc" = __,
  "card_expiry" = __,
  "bill_addr" = __,
  "bill_city" = __,
  "bill_state" = __,
  "bill_zip" = __,
  "bill_phone" = __,
  "current_pw" = __,
}
'''

args = cgi.FieldStorage()

# Call methods on args.

email ='demitri@gmail.com'# args["email"].value
card_nick ='fake123'# args["card_nick"].value
card_number ='4342562157660026'# args["card_number"].value
card_cvc = '426'#args["card_cvc"].value
card_expiry ='02/2016'#args["card_expiry"].value
bill_addr = '97 Bay State Rd'#args["bill_addr"].value
bill_city = 'Boston'#args["bill_city"].value
bill_state = 'MA'#args["bill_state"].value
bill_zip = '02215'#args["bill_zip"].value
bill_phone = '8314615580'#args["bill_phone"].value
current_pw = '12345'#args["current_pw"].value

try:
  x = ordrin_api.ordrin_api.create_cc(email,card_nick,
    card_number, card_cvc, card_expiry, bill_addr,
    bill_city, bill_state, bill_zip, bill_phone,
    current_pw)
  print "Content-type:application/json"
  print
  print json.dumps(x)
except HTTPError as e:
  print '''HTTP/1.1 404 Client 
Content-type:application/json'''
  print
  print "{}"
   

  

