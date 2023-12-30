import math
values = input("Expression: ")
tru = values.split()

int1 = int(tru[0])
arith = tru[1]
int2 = int(tru[2])

if arith == '+':
    result = int1 + int2
elif arith == '-':
    result = int1 - int2
elif arith == '*':
    result = int1 * int2
else:
    result = int1 / int2

print(float(result))