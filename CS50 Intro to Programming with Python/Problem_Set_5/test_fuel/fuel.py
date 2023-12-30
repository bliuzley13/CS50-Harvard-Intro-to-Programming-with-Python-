import math

def main():
    fuelInput = input("Fraction: ")
    percentage = convert(fuelInput)
    result = gauge(percentage)
    print(result)

def convert(fraction):
    if "/" not in fraction:
        raise ValueError
    numDem = fraction.replace(" ", "")
    numDem = numDem.split("/")
    num, dem = numDem[0], numDem[1]
    if "." in num:
        raise ValueError
    if "." in dem:
        raise ValueError
    if num.isdigit() == False:
        raise ValueError
    if dem.isdigit() == False:
        raise ValueError
    num = int(num)
    dem = int(dem)
    if dem == 0:
        raise ZeroDivisionError
    fract = num / dem
    fract = int(fract * 100)
    return fract

def gauge(percentage):
    # while True:
        try:
            if percentage > 100:
                main()
            if percentage == 0:
                return ("E")
            if percentage == 1:
                return ("E")
            if percentage == 100:
                return ("F")
            if percentage == 99:
                return ("F")
            value = str(percentage) + "%"
            return value
        except (ValueError, ZeroDivisionError):
            main()

if __name__ == "__main__":
    main()