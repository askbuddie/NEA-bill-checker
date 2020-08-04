#!/usr/bin/env python3

try:
    from bs4 import BeautifulSoup
    import datetime
    import requests
    import re
    import address
except ModuleNotFoundError:
    print('[-] Module not found. Try pip install -r requirements.txt')
    exit()

banner = \
    '''
  _____  ___    _______       __      
 (\\"   \|"  \  /"     "|     /""\     
 |.\\\   \    |(: ______)    /    \    
 |: \.   \\\  | \/    |     /' /\  \   
 |.  \    \. | // ___)_   //  __'  \  
 |    \    \ |(:      "| /   /  \\\  \ 
  \___|\____\) \_______)(___/    \___) 
 ------------Bill Checker------------
 -Easy way to check Electricity Bill-
 ____________________________________                                    
'''

print(banner)

def getAreaCode(ads):
    for i in address.address:
        if ads in i:
            return (address.address[i])
    return "Not Found."

x = datetime.datetime.now()

d = x.strftime("%b-%y").upper()
date = x.strftime("%m/%d/%Y")
print("Today's date: | " + date + ' |')


sc = input("\nEnter your Sc. No. : ")
custid = input("Enter Customer id: ")

add = input("Enter your NEA Location : ").upper()

ad = getAreaCode(add)

try:
    int(ad)
except Exception:
    print("[-] NEA Location not found!")
    exit(0)

def exit2():

    print('\n [+] Our Site: www.askbuddie.com\n [+] Join Us: www.fb.com/groups/askbuddie\n [+] Our FB page: www.fb.com/askbuddie\n [+] ABOS: https://github.com/askbuddie')
    print('\nThanks for using NEA Bill Checker...\n\n')
    exit()

try:
    int(custid)
except Exception:
    print("\n[-] Customer id must be interger.")
    exit2()


parameters = {'NEA_location': ad, 'sc_no': sc,
              'consumer_id': custid, 'fromdate': '2/28/2017', 'todate': date}
try:
    r = requests.post(
        'https://www.neabilling.com/viewonline/viewonlineresult/', params=parameters)
except Exception:
    print("\n[-] Something went Wrong, Try again later.")
    exit2()

if 'No Records' in r.text:
    print(
        "\n[-] Record not found. You entered\n wrong information.")
else:
    soup = BeautifulSoup(r.text, "html.parser")
    th1 = ""
    for th in soup.find_all("td"):
        th1 += str(th)

    nameSoup  = re.findall('<td style="font-size:14px">.*</td>', th1)[0]
    nameSoup = BeautifulSoup(nameSoup, "html.parser")

    name = ""

    for td in nameSoup.find_all("td"):
        name = td.text

    items = []
    newList = []

    lastRecord = ""

    for td in soup.find_all("tr"):
       lastRecord = td
       items.append(lastRecord)

    amount = items[-1]
    if amount.text != "":
        newList.append(amount.text.split())
    amount = newList[-1][-1]

    if 'UN-PAID' in r.text:
        print(' Hello ' + name + ", You have to pay RS  " + amount)
    elif 'ConsumerId must be' in r.text:
        print("Please enter your numeric Customer ID.")
    else:
        print("Hello " + name + ", your amount has been paid!")

exit2()
