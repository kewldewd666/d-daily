import json
import gspread
from punches import employee_hours
from collections import OrderedDict
from oauth2client.client import SignedJwtAssertionCredentials

alpha_employees = OrderedDict(sorted(employee_hours.items()))

json_key = json.load(open('ddaily-982286e5cb7b.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'].encode(),
                                            scope)

gc = gspread.authorize(credentials)

wks = gc.open("test-sheet").sheet1


'''
Update Names (doesn't want to work in a fucntion)
'''


num = 2
for key, value in alpha_employees.iteritems():
    wks.update_cell(num, 2, key)
    num += 1

'''
writes down ONE column from an ordered dictionary with lists,
starting at a specific index of the lists
'''


def write_col_from_dic_wlists(dic, start_row, start_col, list_index):
    for key, value in dic.iteritems():
        wks.update_cell(start_row, start_col, value[list_index])
        start_row += 1


def write_many_columns_of_dic_wlists(dic, start_row, start_col):
    i = 0
    list_index = 0
    while i < len(dic.items()[0][1]):
        write_col_from_dic_wlists(dic, start_row, start_col, list_index)
        list_index += 1
        start_col += 1
        i += 1

write_many_columns_of_dic_wlists(alpha_employees, 2, 3)
