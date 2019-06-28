#!/usr/bin/env python
import requests
import re
import datetime

x = datetime.datetime.now()

date = x.strftime("%m/%d/%Y")
print "Today: " + date
sc = raw_input("Enter Sc. no. from your bill: ")
custid = raw_input("Enter Customer id: ")

add = raw_input("Enter your NEA Location as in your Bill: ").upper()

file = 'db/a.txt'

with open(file) as a:
	x = a.read()
	if add in x:
		address = ''.join(re.findall(add + " =.*", x)).replace(add+" = ", '')
	else:
		print "Location not found!"

parameters = {'NEA_location':address, 'sc_no': sc, 'consumer_id': custid, 'Fromdatepicker': '2/28/2017', 'Todatepicker': date}
# # print parameters

r = requests.post('https://www.neabilling.com/viewonline/viewonlineresult/', params=parameters)
# # print(r.url)
if 'No Records Found.' in r.text:
	print "Some of your information is incorrect. Records not found."
else:
	a = "".join(re.findall("Customer .*", r.text))
	name = a[45:][::-1][6:][::-1]
	print name

	if 'UN-PAID' in r.text:
		print "Amount not paid!"
	else:
		print "Amount has been paid!"
# print r.text
