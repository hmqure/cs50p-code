import sys
import requests

sys = sys.argv

if sys[1].isdigit() is True:
    print(sys[1])

else:
    sys.exit("Command-line argument is not a number")

