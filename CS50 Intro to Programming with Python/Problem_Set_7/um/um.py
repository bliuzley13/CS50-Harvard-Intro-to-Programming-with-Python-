import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    #Idea with using a regular expression
    #Regular Expression that does not count "um" if there are letters around it or like yum
    umCheck = r"(?<![a-zA-Z])um(?![a-zA-Z])"
    #does the counting part of the um
    umCount = len(re.findall(umCheck, s, flags=re.IGNORECASE))
    #returns number of ums
    return umCount

    #Idea thought of working with splitting the words as necessary
    # wordMultiple = s.split()
    # umCount = 0
    # for i in range(len(words)):
    #     word = wordMultiple[i].lower()
    #     if word == "um":


if __name__ == "__main__":
    main()