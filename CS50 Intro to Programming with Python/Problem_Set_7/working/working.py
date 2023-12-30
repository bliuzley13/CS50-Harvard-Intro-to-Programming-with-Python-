import re
#import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    #Regular Expression Version
    formatCheck = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if formatCheck:
        #This groups multiple characters being considered as a single unit
        parts = formatCheck.groups()
        #These are the parts for hours not existing as 13 AM or PM
        if int(parts[1]) > 12 or int(parts[5]) > 12:
            raise ValueError
        #This is the starting Time of the input
        startTime = changeFormat(parts[1], parts[2], parts[3])
        #This is the ending Time of the input
        endTime = changeFormat(parts[5], parts[6], parts[7])
        #This is the result that will be printed out
        return startTime + ' to ' + endTime
    else:
        #In case the regular expression does not work
        raise ValueError

#This function is what will change the format of each time
def changeFormat(hr, min, ampm):
    #This will do the work regarding PM
    if ampm == "PM":
        #if 12 PM, then it will stay as 12:00
        if int(hr) == 12:
            reHour = 12
        #for values like 1 PM, it will change to 13:00
        else:
            reHour = int(hr) + 12
    #This is regarding the work with the AM
    else:
        #12 AM is 0:00
        if int(hr) == 12:
            reHour = 0
        #Whatever time like 1 AM will be 1:00
        else:
            reHour = int(hr)
    #regarding minutes if there is none in the input like 9 AM
    if min == None:
        reMin = ':00'
        reTime = f"{reHour:02}" + reMin
    #for when something is like 9:02 AM
    else:
        reTime = f"{reHour:02}" + ":" + min
    return reTime

if __name__ == "__main__":
    main()

    #Code that looks at the spacing and position of the items
    #Does not fit every work case and is sloppy
    # if "-" in s:
    #     raise ValueError("Has to be 'to' in the string for the time")
    # startTime, endTime = s.split(" to ")
    # startParts = startTime.replace(" AM", "").replace(" PM", "").split(":")
    # endParts = endTime.replace(" AM", "").replace(" PM", "").split(":")
    # startHours = int(startParts[0])
    # endHours = int(endParts[0])
    # if "PM" in startTime:
    #     startHours += 12
    # if "PM" in endTime:
    #     endHours += 12
    # startMins = startParts[1] if len(startParts) > 1 else "00"
    # endMins = endParts[1] if len(endParts) > 1 else "00"
    # if int(startMins) > 59 or int(endMins) > 59:
    #     raise ValueError("Minutes between 0 & 59")
    # return f"{startHours:02d}:{startMins} to {endHours:02d}:{endMins}"

