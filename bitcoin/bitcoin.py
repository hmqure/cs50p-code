import sys
import requests

sys = sys.argv

if len(sys) == 2:
    if sys[1].isdigit() is True:

        try:

        except requests.RequestException:
            

    else:
        sys.exit("Command-line argument is not a number")

else:
     sys.exit("Missing command-line argument")

