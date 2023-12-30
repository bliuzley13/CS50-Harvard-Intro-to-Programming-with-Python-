def main():
    #input
    vers_inp = input("Your input: ")
    #main code for result
    print("camelCase: " + vers_inp)
    print("snake_case: " + snake_case(vers_inp))

def snake_case(val):
    #string meant for outputting
    val2 = ""
    #i works as a letter in this case
    for i in val:
        if i.isupper() == True:
            val2 += "_"
            val2 += i.lower()
        else:
            val2 += i
    return val2

#executes main function
if __name__ == "__main__":
    main()