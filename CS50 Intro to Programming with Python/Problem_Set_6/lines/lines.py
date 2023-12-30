import sys

def main():
    #checks the command line input
    command_line_checker_args()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    #checks if the file is not in the folder
    except FileNotFoundError:
        sys.exit("File does not exist")
    #counts the lines in a file
    cnt_lns = 0
    for line in lines:
        if line_check(line) == False:
            cnt_lns += 1
    print(cnt_lns)

#checks the argument being entered
def command_line_checker_args():
    num_args = len(sys.argv) - 1
    #checks if argument is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    #checks if there are too few or too less arguments
    if num_args < 1:
        sys.exit("Too few command-line arguments")
    if num_args > 1:
        sys.exit("Too many command-line arguments")


#checks if the line is valid
def line_check(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
