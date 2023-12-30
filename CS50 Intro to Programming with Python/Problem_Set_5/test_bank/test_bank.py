from bank import value

def main():
    #test cases for bank
    test_zero()
    test_20()
    test_100()

def test_zero():
    assert value('hello') == 0
def test_20():
    assert value('hi') == 20
    assert value('Hi') == 20
def test_100():
    assert value('Whats Up') == 100

# #runs main function
if __name__ == "__main__":
        main()