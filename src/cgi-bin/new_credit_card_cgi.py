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
  "card_number" = __,
  "card_cvc" = __,
  "card_expiry" = __,
  "bill_addr" = __,
  "bill_addr2" = __, default None
  "bill_city" = __,
  "bill_state" = __,
  "bill_zip" = __,
  "bill_phone" = __,
  "current_pw" = __,
}
'''

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.

email = args["email"].value
nick = args["nick"].value
card_number = args["card_number"].value
card_cvc = args["card_cvc"].value
card_expiry = args["card_expiry"].value
bill_addr = args["bill_addr"].value
bill_addr2 = args["bill_addr2"].value
bill_city = args["bill_city"].value
bill_state = args["bill_state"].value
bill_zip = args["bill_zip"].value
bill_phone = args["bill_phone"].value
current_pw = args["current_pw"].value

ordrin_api.ordrin_api.create_cc[email, nick, card_number,
    card_cvc, card_expiry, bill_addr, bill_addr2,
    bill_city, bill_state, bill_zip, bill_phone,
    current_pw]


