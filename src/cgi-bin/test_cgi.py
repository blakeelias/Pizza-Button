#!/usr/bin/env python

import cgi
import cgitb

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.


print "{"

for i in args.keys():
  if i != 0:
    print "\targ{0}:\t{1}\n".format(i, args[i].value)

print "}"
