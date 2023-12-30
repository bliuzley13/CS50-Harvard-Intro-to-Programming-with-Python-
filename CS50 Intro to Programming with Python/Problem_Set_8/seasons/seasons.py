from datetime import datetime, date
import sys
import re
import inflect

i = inflect.engine()

def main():
    #input code
    DaYs = checkValid(input("Date of Birth: "))
    print(ageMinWords(DaYs))

def checkValid(strValue):
    #pattern to check string input
    checkPattern = r"^\d{4}-\d{2}-\d{2}$"
    #checks if the input is valid or not
    if bool(re.match(checkPattern, strValue)) == True:
        #returns main when calculating age in mins
        return ageDays(strValue)
    else:
        sys.exit("Invalid date")

#Intended to find out the age of a person in days
def ageDays(inputValue):
    #Use to find the current date
    currentDate = date.today()
    #Current date in YYYY-MM-DD (isoformat)
    reformDate = currentDate.isoformat()
    #Intended to have a pattern that will help to subtract the dates in isoformat
    dateFormatRule = "%Y-%m-%d"
    #Sets up the dates before subtracting
    bdayDate = datetime.strptime(inputValue, dateFormatRule)
    currDate = datetime.strptime(reformDate, dateFormatRule)
    #Subtracted Date
    result = currDate - bdayDate
    #Days between the two dates
    dayZ = result.days
    #Returns number of days
    return dayZ

def ageMinWords(days):
    #converts days to number of minutes
    minuteInt = days*24*60
    #Changes the minutes to words
    wordMin = i.number_to_words(minuteInt, andword="")
    #Capitalizes the word
    wordMin2 = wordMin.capitalize()
    #Removes the subsequent commas
    # words = [word.strip() for word in wordMin2.split(',')]
    # formWords = " ".join(words)
    #returns the final result
    return wordMin2 + " minutes"

if __name__ == "__main__":
    main()