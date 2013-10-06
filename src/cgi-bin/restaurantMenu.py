#!/usr/bin/env python
import sys

import cgi
import cgitb
from ordrin_api import ordrin_api
import json

def itemString(item, levelDepth):
    s = ' '*levelDepth + '<div class="item" id="menuItem-' + str(item['id']) + '">\n'
    
    s += ' '*(levelDepth+4) + '<div class="name">' + item['name'] + '</div>\n'
    s += ' '*(levelDepth+4) + '<div class="description">' + item['descrip'] + '</div>\n'
    
    if float(item['price']) > 0:
        s += ' '*(levelDepth+4) + '<div class="price">' + item['price'] + '</div>\n'
        s += ' '*(levelDepth+4) + '<input type="text" class="quantity" />\n'
    
    if 'children' in item:
        for child in item['children']:
            s += itemString(child, levelDepth + 4)
    
    s += ' '*levelDepth + '</div>\n'
    return s

print "Content-type:text/html"
print

args = cgi.FieldStorage()

# Call methods on args.

'''
Expects the following arguments: 
{
    'rid': __
}

Returns a list of things on the menu
'''

# Prevent API call from printing a line that we don't want in the output
save_stdout = sys.stdout
sys.stdout = open('trash', 'w')

details = ordrin_api.restaurant_details(args["rid"].value)

sys.stdout = save_stdout
# End prevent printing

for item in details['menu']:
    try:
        item['descrip'].lower().index('pizza')
        print itemString(item, 0)
    except:
        pass

#print(json.dumps(details['menu']))


