import sys
import requests
import json

sys = sys.argv

x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if len(sys) == 2:
    if sys[1].isdigit() is True:
        try:
            y = x.json()
            print(y["Bitcoin"])
        except requests.RequestException:
            sys.exit("Psych")


    else:
        sys.exit("Command-line argument is not a number")

else:
     sys.exit("Missing command-line argument")

