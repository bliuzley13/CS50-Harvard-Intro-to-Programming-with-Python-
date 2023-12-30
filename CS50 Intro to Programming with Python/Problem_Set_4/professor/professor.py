#random import
import random

def main():
    #gets the level
    value = get_level()
    #generates the problems
    result = generate_integer(value)
    #output
    print("Score: " + str(result))

def get_level():
    #has levels that are accepted only from 1-3
    while True:
        try:
            lvl = int(input("Level: "))
            if 0 < lvl <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            pass
    return lvl



def generate_integer(level):
    #while True:
        e_val = 0
        finale = 0
        inty = 0

        #meant to create 10 problems
        for _ in range(10):
                #levels that generate types of numbers
                if level == 1:
                    op1 = random.randint(0, 9)
                    op2 = random.randint(0, 9)
                elif level == 2:
                    op1 = random.randint(10, 99)
                    op2 = random.randint(10, 99)
                else:
                    op1 = random.randint(100, 999)
                    op2 = random.randint(100, 999)
                #generated numbers sum
                val = op1 + op2
                #equation to solve
                print(f"{op1} + {op2} =", end='')
                #answer to the equation
                ans = int(input(" "))


                #if answer is right, adds 1 to score
                if val == ans:
                    #score adding point
                    finale += 1
                    #count of an equation made
                    inty += 1
                    #wrote 10 questions
                    if inty == 10:
                        #finishes part of code
                        break

                #checks the 3 mistakes of EEE
                if val != ans:
                    #first fail
                    print("EEE")
                    #while loop for second and third fail
                    while e_val < 2:
                        #counts the error
                        e_val += 1
                        #equation to solve
                        print(f"{op1} + {op2} =", end='')
                        #answer to the equation
                        ans = int(input(" "))
                        #fail
                        if val != ans:
                            print("EEE")
                    #correct answer
                    print(f"{op1} + {op2} = {val}")

        #score result
        return finale

if __name__ == "__main__":
    main()