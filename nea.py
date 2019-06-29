#!/usr/bin/env python
import requests
import re
import datetime

x = datetime.datetime.now()

d = x.strftime("%b-%y").upper()
# print d
date = x.strftime("%m/%d/%Y")
print "Today: " + date
sc = raw_input("Enter Sc. no. from your bill: ")
custid = raw_input("Enter Customer id: ")

add = raw_input("Enter your NEA Location as in your Bill: ").upper()

file = 'address.txt'

with open(file) as a:
	x = a.read()
	addres = ''
	address1 = add
	address2 = add + " DC"

	if address1 or address2 in x:
		if address2 in x:
			address = ''.join(re.findall(address2 + ".* =.*", x)).replace(address2 + " = ", '')
		else:
			address = ''.join(re.findall(address1 + " =.*", x)).replace(address1 + " = ", '')

	else:
		print add + " Not found!"
		exit(1)
if (address == '' or sc == '' or custid == ''):
	print "You forgot to enter something!"
	exit(1)
else:
	parameters = {'NEA_location':address, 'sc_no': sc, 'consumer_id': custid, 'Fromdatepicker': '2/28/2017', 'Todatepicker': date}
	# # print parameters

	r = requests.post('https://www.neabilling.com/viewonline/viewonlineresult/', params=parameters)
	# # print(r.url)
	if 'No Records' in r.text:
		print "Some of your information is incorrect. Records not found."
	else:
		a = "".join(re.findall("Customer .*", r.text))
		name = a[45:][::-1][6:][::-1]
		print name

		am = ''.join(re.findall( d + '([\s\S]*?)</tr>', r.text, re.MULTILINE))
		b = re.findall("<td>.*</td>", am)
		amount = b[1].replace("<td>", "").replace("</td>", "")

		if 'UN-PAID' in r.text:
			print "Rs. " + amount + " hasnot been paid!"
		elif 'ConsumerId must be' in r.text:
			print "Please eter your numeric Customer ID."
		elif 'Advance' in r.text:
			print "Rs. " + amount.replace('-', '') + " has been paid in Advance!"
		else:
			print "Rs. " + amount + " has been paid!"
	# print r.text
