import string
import re

pattern = r'\d+[a-zA-Z]\d+'

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #1st condition
    #For less than 2 in a string
    if len(s) < 2:
        return False
    #For more than 7 in a string
    if len(s) > 6:
        return False
    #For starting with two letters
    if len(s) >= 2:
        if s[0].isalpha() != True:
            return False
        if s[1].isalpha() != True:
            return False
    #Checks if all are letters
    if s.isalpha():
        return True
    #2nd condition
    #For min of 2 letters and max of 6 letters
    if (2 <= len(s) <= 6) == True:
        match = re.search(pattern, s)
        if match:
            return False
    else:
        return False

    #3rd Condition
    #For not having numbers in the middle of a plate
    for i in s:
        if s[-1].isdigit() != True:
            return False
    #For first number not being zero
        if i.isdigit():
            if i == "0":
                return False
            else:
                break

    #4th condition
    for j in s:
        #No Periods
        if j == ".":
            return False
        #No Spaces
        if j == " ":
            return False
        #No Punctuation
        if j in string.punctuation:
            return False

    #When not hitting any False Results
    return True

if __name__ == "__main__":
    main()