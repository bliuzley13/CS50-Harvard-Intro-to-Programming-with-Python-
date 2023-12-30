tacq = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

try:
    prices = 0
    # while True:
        #format
    while True:
        item_input = input("Item: ")
        item_spt = item_input.split(" ")
        item_cap = [i.capitalize() for i in item_spt]
        item_fmt = ' '.join(item_cap)
        if item_fmt in tacq:
            prices += tacq[item_fmt]
        else:
            pass
        total = "Total: $" + str(prices) + "0"
        print(total)

except EOFError:
    total = "Total: $" + str(prices) + "0"
    print(total)
