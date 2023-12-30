#import code
import math
import requests
import sys

#response code
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#having no argument
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
#argument after python file
arg1 = sys.argv[1]

try:
    ag = float(arg1)
    if response.status_code == 200:
        amount = response.json()
        val1 = amount["bpi"]["USD"]["rate_float"]
        #val1 is the rate
        final = float(val1) * ag
        #formatted version of the output
        print(f"${final:,.4f}")

except ValueError:
    #if argument is not a float
    sys.exit("Command-line argument is not a number")

except requests.RequestException:
    pass