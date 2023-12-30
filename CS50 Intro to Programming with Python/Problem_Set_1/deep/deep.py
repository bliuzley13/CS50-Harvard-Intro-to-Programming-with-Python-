value = input(str("Input Value: "))
value = value.lower()
value = value.strip()

if value == "42":
    print("Yes")
elif value == "forty two":
    print("Yes")
elif value == "forty-two":
    print("Yes")
else:
    print("No")