#imports in the required code to run the program
from tabulate import tabulate
import sys
import csv

def main():
    comm_line_check()
    #empty table
    tbl = []
    try:
        #opens csvfile
        with open(sys.argv[1], "r") as csvfile:
            #reads csv files
            reader = csv.reader(csvfile)
            #adds a line to the table
            for row in reader:
                tbl.append(row)
    #says when file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    #returns output with grid
    print(tabulate(tbl[1:], headers = tbl[0], tablefmt="grid"))

def comm_line_check():
    #checks if file is csv file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    #checks if there are more or less arguments inputted to command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()