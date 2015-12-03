import json
import gspread
from punches import employee_hours
from collections import OrderedDict
from oauth2client.client import SignedJwtAssertionCredentials

alpha_employees = OrderedDict(sorted(employee_hours.items()))

json_key = json.load(open('ddaily-982286e5cb7b.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

wks = gc.open("test-sheet").sheet1

'''
Update Names
'''
# for key, value in alpha_employees.iteritems():
#     print key

#print alpha_employees

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 2, key)
    num += 1

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 3, value[0])
    num += 1

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 4, value[1])
    num += 1

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 5, value[2])
    num += 1

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 6, value[3])
    num += 1

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 7, value[4])
    num += 1

num = 1
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 8, value[5])
    num += 1
