import math

def main():
    fuelInput = input("Fraction: ")
    result = fuel_Gauge(fuelInput)
    print(result)

def fuel_Gauge(value):

    while True:
        try:
            if "/" not in value:
                raise ValueError
            numDem = value.split("/")
            num, dem = numDem[0], numDem[1]
            if "." in num:
                raise ValueError
            if "." in dem:
                raise ValueError
            num = int(num)
            dem = int(dem)
            fract = num / dem
            if dem == 0:
                raise ZeroDivisionError
            if fract > 1:
                main()
            if fract == 0:
                return ("E")
            if fract == (0.01):
                return ("E")
            if fract == 1:
                return ("F")
            if fract == (0.99):
                return ("F")
            value = str(int(round(fract * 100))) + "%"
            return value
        except (ValueError, ZeroDivisionError):
            main()
        break

if __name__ == "__main__":
    main()