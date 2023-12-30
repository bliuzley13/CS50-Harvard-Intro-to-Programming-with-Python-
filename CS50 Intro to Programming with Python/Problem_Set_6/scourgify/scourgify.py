import csv
import sys

blank = []

def main():
    #Does the command-line arguments number check
    arg_check()
    #takes in to check
    input_csv = sys.argv[1]
    try:
        #Meant to create and make a new csv file that will written in
        with open(sys.argv[1], 'r') as csv_input, open(sys.argv[2], 'w') as csv_output:
            #Reads the Data
            rdr = csv.DictReader(csv_input)
            #Goes through every line in before.csv
            for row in rdr:
                #splits the name by first and last name
                name = row["name"].split(",")
                #has a remade line that is reordered from the original csv file
                blank.append({'first': name[1].lstrip(), "last": name[0], "house": row["house"]})
            #Writes the data to the new csv file, fieldnames being to confirm the column headers
            wrtr = csv.DictWriter(csv_output, fieldnames=["first", "last", "house"])
            #writes the header line
            wrtr.writerow({"first": "first", "last": "last", "house": "house"})
            #Writes a row to csv when checking through the data which is in blank
            for row in blank:
                #Writes the row in the csv file which is the data
                wrtr.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
    #Certain csv not being in the code
    except FileNotFoundError:
        sys.exit("Could not read " + input_csv)

#Checks how many command-line arguments exist
def arg_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #CSV check
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

#Runs the main file
if __name__ == "__main__":
    main()