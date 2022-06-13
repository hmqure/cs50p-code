import sys
import requests
import json

sys = sys.argv

if len(sys) == 2:
    if sys[1].isdigit() is True:

        try:
            print(request.get())
        except requests.RequestException:


    else:
        sys.exit("Command-line argument is not a number")

else:
     sys.exit("Missing command-line argument")

