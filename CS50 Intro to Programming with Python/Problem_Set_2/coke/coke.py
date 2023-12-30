import math
debt = 50
while (debt != 0):
    print("Amount Due: " + str(debt))
    insrt = int(input("Insert Coin: "))
    if insrt == 5:
        debt = debt - insrt
    elif insrt == 10:
        debt = debt - insrt
    elif insrt == 25:
        debt = debt - insrt
    else:
        debt = debt
    if debt < 0:
        break
print("Change Owed: " + str(abs(debt)))
