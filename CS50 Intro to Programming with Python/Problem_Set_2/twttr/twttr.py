inp = input("Input: ")
outp = ""
vwls = ["a", "e", "i", "o", "u"]

for i in inp:
    if i.lower() in vwls:
        outp += ""
    else:
        outp += i
print(outp)