import csv

#   This dictionary stores all the info needed
employee_hours = {}


def create_employee(name):
    '''
    [billed hours, unbilled hours, clock hours, hrvt %, billed %]
    '''
    employee_hours[name] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def add_unbill_hrs(name, hours):
    employee_hours[name][0] += hours


def add_bill_hrs(name, hours):
    employee_hours[name][1] += hours


def add_harvest_total(name, hours):
    employee_hours[name][2] += hours


def add_clock_hrs(name, hours):
    employee_hours[name][3] += hours


def add_harvest_perc(name, hours):
    employee_hours[name][4] += hours


def add_billed_perc(name, hours):
    employee_hours[name][5] += hours


def percentage(part, whole):
    if whole != 0:
        return float(part)/float(whole)
    else:
        return 0.0

'''
----------------Process the Harvest CSV file------------------------
      First          Last            Hours       Billable 'Yes' or 'No'
    row[12]        row[13]          row[6]        row[10]
'''

f = open('harvest.csv')
csv_f = csv.reader(f)
f.next()

for row in csv_f:
    name = row[12]
    hours = round(float(row[6]), 2)
    billable = True if row[10] == 'Yes' else False
    if name not in employee_hours:
        create_employee(name)
    add_harvest_total(name, hours)
    if billable:
        add_bill_hrs(name, hours)
    else:
        add_unbill_hrs(name, hours)

'''
------------Process the Icon CSV file---------------
     First           Last          Hours
     row[0]         row[2]        row[27]
'''

g = open('icon.csv')
csv_g = csv.reader(g)
g.next()

for row in csv_g:
    name = row[0]
    mins = round(float(row[27]), 2)
    hours = round(mins/60, 2)
    if name not in employee_hours:
        create_employee(name)
    add_clock_hrs(name, hours)

'''
----------Compute Percentages-----------------
'''

for employee in employee_hours:
    # harvest_unbilled = employee_hours[employee][0]
    harvest_billed = employee_hours[employee][1]
    harvest_total = employee_hours[employee][2]
    clock_total = employee_hours[employee][3]
    # set to harvest total if they don't clock in
    if clock_total == 0.0:
        clock_total = harvest_total
    harvest_perc = percentage(harvest_total, clock_total)
    billed_perc = percentage(harvest_billed, clock_total)

    add_harvest_perc(employee, harvest_perc)
    add_billed_perc(employee, billed_perc)
