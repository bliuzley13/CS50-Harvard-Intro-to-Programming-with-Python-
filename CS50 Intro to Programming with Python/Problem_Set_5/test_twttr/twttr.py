import re

def main():
    #input
    inp = input("Input: ")
    #output
    outp = shorten(inp)
    #result
    print(outp)

def shorten(word):
    vwls = ["a", "e", "i", "o", "u"]
    inp2 = ""
    #does the removal of vowels from string
    for i in word:
        if i.lower() in vwls:
            inp2 += ""
        else:
            inp2 += i
    return inp2

if __name__ == "__main__":
    main()