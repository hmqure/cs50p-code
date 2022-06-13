import sys
import requests
import json

sys = sys.argv
floatsys = float(sys[1])

x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if len(sys) == 2:
    if sys[1].isdigit() is True:
        try:
            y = x.json()
            rate = y["bpi"]['USD']['rate']
            newrate = rate.replace(',','')
            total = float((float(newrate))*float(sys[1]))
            print("$"+"{:,}".format(total))



        except requests.RequestException:
            sys.exit("Psych")


    else:
        sys.exit("Command-line argument is not a number")

else:
     sys.exit("Missing command-line argument")

