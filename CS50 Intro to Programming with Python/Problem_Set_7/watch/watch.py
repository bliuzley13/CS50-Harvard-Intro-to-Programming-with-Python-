import re
# import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):

    #Idea of code that tried to work with checking code and
    # resultWebsite = ""
    # if re.search(r"")
    # for argIndex, argument in enumerate(sys.argv[1:], start=1):
    #     if "http" in s:
    #         resultWebsite = resultWebsite + "https://"
    #     if "www.youtube.com" in s:
    #         resultWebsite = resultWebsite + "youtu.be/"
    #     checker = re.search(r'embed\/([a-zA-Z0-9\-_]+)', s)
    #     enDER = checker.group()
    #     resultEnd = enDER.split('/')
    #     final = resultWebsite + resultEnd[1]
    #     return final

    #checks for the conditions with the http and the youtube link
    if "http" and "www.youtube.com" in s:
                pass
    #checks if there is the iframe being entered in the input
    if re.search(r"<iframe(.)*><\/iframe>", s):
        #the pattern that looks for the embed part of the youtube video since that is in the link
        webPattern = re.search(r"(\/embed\/)([a-z_A-Z_0-9]+)", s)
        if webPattern:
            #sets the pattern into groups which are enclosed by the parentheses
            enDER = webPattern.groups()
            #output of the intended website with the location of the youtube link
            return "https://youtu.be/" + enDER[1]


if __name__ == "__main__":
    main()