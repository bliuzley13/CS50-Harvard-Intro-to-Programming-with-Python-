import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    #Checks to validate the email and result is a boolean
    result = validators.email(s)
    #Returns Valid or Invalid
    if result == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()