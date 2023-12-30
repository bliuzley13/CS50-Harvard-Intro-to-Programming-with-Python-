def main():
    meal_inp = input("What time is it? ")
    result = convert(meal_inp)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")
    else:
        print('')

def convert(time):
    cnv = time.split(":")
    hr = int(cnv[0])
    mins = int(cnv[1]) / 60
    tm = hr + mins
    return tm

if __name__ == "__main__":
    main()