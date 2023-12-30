#Modules which can be used
import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Previous conditions
    # #Condition checkers
    # if ip.count(".") == 3:
    #     pass
    # else:
    #     return False
    # if len(values) == 4:
    #     pass
    # else:
    #     return False

    #does the check with a regular expression
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        #creates a list from the input
        values = ip.split(".")
        #does the range checking for each integer
        for i in values:
            if int(i) <= 255 and int(i) >= 0:
                pass
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()