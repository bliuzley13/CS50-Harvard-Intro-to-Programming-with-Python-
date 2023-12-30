from numb3rs import validate

def main():
    test_addresses()
    test_formats()
    # test_words()

def test_addresses():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.333.444.555') == False

def test_formats():
    assert validate('1') == False
    assert validate('1.2') == False
    assert validate('1.2.3') == False
    assert validate('1.2.3.4') == True

def test_words():
    assert validate('cat') == False
    assert validate('dog') == False

if __name__ == "__main__":
    main()