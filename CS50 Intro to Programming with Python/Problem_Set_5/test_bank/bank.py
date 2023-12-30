def main():
    mone = input(str("Greeting: "))
    mone = mone.lower()
    result = val(mone)
    conclude = "$" + str(result)
    print(conclude)

def value(greeting):

    intent_word = "hello"

    if intent_word in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
