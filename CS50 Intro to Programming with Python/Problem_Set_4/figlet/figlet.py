#Figlet module
from pyfiglet import Figlet
#For arguments and sys.exit
import sys

#Runs Figlet as a variable
figlet = Figlet()
#Number of arguments
num_arg = len(sys.argv)
#list of available fonts
s = figlet.getFonts()
#First argument after figlet.py file
arg1 = sys.argv[1]
#Checks if -f exists
if arg1 == "-f":
    pass
else:
    #sys.exit code
    sys.exit("Invalid Usage")

#Sees if there is another argument after the intended -f
if num_arg > 2:
    #Second argument after figlet.py file
    arg2 = sys.argv[2]
    #Checks if font is in the font list
    if arg2 in s:
        pass
    else:
        #sys.exit code
        sys.exit("Invalid Usage")
    #Sets the font
    figlet.setFont(font=arg2)
    #Input code
    result = input("")
    #Output code
    print(figlet.renderText(result))


