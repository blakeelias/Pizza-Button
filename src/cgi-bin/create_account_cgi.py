import ordrin_api

'''
Expects the following arguments:
args = {
  "email" = __,
  "pw" = __,
  "first_name" = __,
  "last_name" = __,
}
'''

print "Content-type:application/json"
print

args = cgi.FieldStorage()

# Call methods on args.
email = args["email"]
pw = args["pw"]
first_name = args['first_name']
last_name = args['last_name']

x = ordrin_api.ordrin_api.create_account(email, pw,
    first_name, last_name)
