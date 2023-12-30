#Helps with counting in my code
from collections import Counter

#Lists with Grocery Items and number of each type of item
items = []

try:
    while True:
        #Input
        groc_input = input("")
        #Uppercase for list
        groc_out = groc_input.upper()
        #Adding to List
        items.append(groc_out)

except EOFError:
    #Ordering
    items.sort()
    #Counting Duplicates for each number
    items_count = Counter(items)
    #Prints out List
    for i, j in items_count.items():
        print(j, i)