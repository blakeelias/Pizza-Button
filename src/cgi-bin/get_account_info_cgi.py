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

x =   ordrin_api.ordrin_api.get_account_info(email,
    current_pw)

print x
'''
Example return:
{u'em': u'artemisfowl5900@yahoo.com', u'first_name': u'demitri', u'last_name': u'nava', u'pw': u'03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', u'_id': u'5250d585d487f2701e00002e'}
'''
