#random module
import random

#Reprompt part
while True:
    #Keeps going until input is positive integer
    try:
        #input
        lvl = int(input("Level: "))
        #if it is 0 or less than 0
        if lvl <= 0:
            raise ValueError
        break
    #checks for non integers
    except ValueError:
        pass
#meant for comparing the variables
random_lvl = random.randint(1, lvl)
while True:
    #keeps going until result is "Just right!"
    try:
        #guess input
        guess_lvl = int(input("Guess: "))
        #guess can not be negative
        if guess_lvl < 0:
            raise ValueError
        #guess is right
        if guess_lvl == random_lvl:
            print("Just right!")
            #finishes the program
            break
        #guess is not right
        elif guess_lvl > random_lvl:
            print("Too large!")
        else:
            print("Too small!")
    #checks for input not an integer
    except ValueError:
        pass
