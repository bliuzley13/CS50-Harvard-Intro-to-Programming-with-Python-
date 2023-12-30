#importing inflect
import inflect
#engine to help run code
inst = inflect.engine()
#empty list
names=[]
#gathers the names until Ctrl+D
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
print(names)
#List in output
#if there was one name
if len(names) == 1:
    lst = names[0]
#if there were more than 2 names
elif len(names) > 2:
    lst = ', '.join(names[:-1]) + ', and ' + names[-1]
#if there were 2 names
else:
    lst = ', '.join(names[:-1]) + ' and ' + names[-1]
#concatenated string
outpt = "Adieu, adieu, to " + lst
#output
print(outpt)