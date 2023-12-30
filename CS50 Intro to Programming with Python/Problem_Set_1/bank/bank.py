value = input(str("Greeting: "))
value = value.lower()
intent_word = "hello"

if intent_word in value:
    print('$0')
elif value[0] == 'h':
    print('$20')
else:
    print('$100')