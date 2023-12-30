from plates import is_valid

def main():
    test_check()
    test_check2()
    test_check3()

def test_check():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
def test_check2():
    assert is_valid('CS50P') == False
    assert is_valid('PI3.14') == False
def test_check3():
    assert is_valid('123123') == False
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False

if __name__ == "__main__":
        main()