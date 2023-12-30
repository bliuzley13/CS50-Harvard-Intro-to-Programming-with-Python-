months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    #input
    dt = input("Date: ")
    #outputs result
    print(date(dt))

def date(dt):
    #Dates with Slashes
    while True:
        if "/" in dt:
            #Separates lists based on slash
            dt = dt.strip()
            dt_split = dt.split("/")
            #Has the year, month, and day variables
            yr, mnth, dy = dt_split[2], dt_split[0], dt_split[1]
            if mnth in months:
                main()
            #Checks the month and day limits and reprompts accordingly
            if int(mnth) > 12:
                main()
            if int(dy) > 31:
                main()
            #Adds a zero if month and day have a single digit
            if len(mnth) == 1:
                mnth = "-0" + mnth
            else:
                mnth = "-" + mnth
            if len(dy) == 1:
                dy = "-0" + dy
            else:
                dy = "-" + dy
            #Puts string together
            result = (str(yr) + str(mnth) + str(dy))
            #Goes to main function
            return result
        #Dates with Commas
        elif "," in dt:
            #Removes Comma in String
            dt = dt.replace(",", "")
            #Separates lists based on slash
            dt_split = dt.split(" ")
            #Has the year, month, and day variables
            yr, mnth, dy = dt_split[2], dt_split[0], dt_split[1]
            if dt_split[1] in months:
                main()
            #Meant to replace the Month Word with the Digit Counterpart
            if dt_split[0] in months:
                #Used for counting through the months
                monthNum = 0
                #iteration through months
                for i in months:
                    #adds for every month in months accessed by for loop
                    monthNum += 1
                    #Compares if the input month matches dictionary month
                    if dt_split[0] == i:
                        #Replaces word month with digit month
                        mnth = str(monthNum)
            #Checks the month and day limits and reprompts accordingly
            if int(mnth) > 12:
                main()
            if int(dy) > 31:
                main()
            #Adds a zero if month and day have a single digit
            if len(mnth) == 1:
                mnth = "-0" + mnth
            else:
                mnth = "-" + mnth
            if len(dy) == 1:
                dy = "-0" + dy
            else:
                dy = "-" + dy
            #Puts string together
            result = (str(yr) + str(mnth) + str(dy))
            #Goes to main function
            return result
        else:
            main()

#Works by calling main function
if __name__ == "__main__":
    main()