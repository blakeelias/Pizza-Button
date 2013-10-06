#!/usr/bin/env python
import sys

import cgi
import cgitb
import ordrin

# Two different servers:
# ordrin.TEST or ordrin.PRODUCTION
server = ordrin.TEST

ordrin = ordrin.APIs("ordrin.APIsjWSw_CthhgY0afo7hMbN7gd3AlPtKLYtDs2Mf_uituM",server)

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.


