#!/usr/bin/env python

banner = \
'''\033[95m
  _____  ___    _______       __      
 (\\"   \|"  \  /"     "|     /""\     
 |.\\\   \    |(: ______)    /    \    
 |: \.   \\\  | \/    |     /' /\  \   
 |.  \    \. | // ___)_   //  __'  \  
 |    \    \ |(:      "| /   /  \\\  \ 
  \___|\____\) \_______)(___/    \___) 
 ------------Bill Checker------------
\033[93m -Easy way to check Electricity Bill-\033[95m
 ____________________________________                                    
'''

print banner

try:
    import datetime,requests,re
except ModuleNotFoundError:
	print '\n\033[91m[-] Module not found. Try pip install -r requirements.txt'
	exit()


x = datetime.datetime.now()

d = x.strftime("%b-%y").upper()
# print current date
date = x.strftime("%m/%d/%Y")
print "\033[97m           | " + date + ' |'


sc = raw_input("\n\033[92m Enter your Sc. No. : \033[94m")
custid = raw_input("\033[92m Enter Customer id: \033[94m")

add = raw_input("\033[92m Enter your NEA Location : \033[94m").upper()

file = 'address.txt'

def exit2():

	print('\n\033[94m [+] Our Site: www.askbuddie.com\n [+] Join Us: www.fb.com/groups/askbuddie\n [+] Our FB page: www.fbcom/askbuddie\n [+] ABOS: https://github.com/askbuddie')
	print('\n\033[93m Thanks for using NEA Bill Checker...\n\n')
	exit()

with open(file) as a:
	x = a.read()
	address = ''
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

print  ' _____________________________________' 

if (len(add) == 0 or len(sc) == 0 or len(custid) == 0  ):
	print "\n\033[91m [-] Please enter all asked information\n properly."
	exit2()


elif len(address) == 0:
	print "\n\033[91m [-] You entered Invalid Address."
	exit2()

try :
	int(custid)
except Exception:
	print "\n\033[91m [-] Customer id must be interger."
	exit2()
	
else:
	parameters = {'NEA_location':address, 'sc_no': sc, 'consumer_id': custid, 'Fromdatepicker': '2/28/2017', 'Todatepicker': date}
	# # print parameters
	try:
		r = requests.post('https://www.neabilling.com/viewonline/viewonlineresult/', params=parameters)
	except Exception:
		print "\n\033[91m [-] Something went Wrong, Try again later."
		exit2()
		
	# # print(r.url)
	if 'No Records' in r.text:
		print "\n\033[91m [-] Record not found. You entered\n wrong information."
	else:
		a = "".join(re.findall("Customer .*", r.text))
		name = a[45:][::-1][6:][::-1]

		am = ''.join(re.findall( d + '([\s\S]*?)</tr>', r.text, re.MULTILINE))
		b = re.findall("<td>.*</td>", am)
		amount = b[4].replace("<td>", "").replace("</td>", "")
		print '\033[92m'
		if 'UN-PAID' in r.text:
			print ' Hello ' + name + ", You have \n to pay RS  " + amount 
		elif 'ConsumerId must be' in r.text:
			print " Please enter your numeric Customer ID."
		# elif 'ADVANCE' in r.text:
		# 	print " Hello " + name + ", You have \n paid Rs. " + amount.replace('-', '') + "  in Advance!"
		else:
			print " Hello " + name +", Rs. " + amount + " \n has been paid!"

exit2()
