from working import convert
import pytest

def main():
    test_wrong()
    test_time()
    test_wrong_hour_or_minute()

def test_wrong():
    with pytest.raises(ValueError):
        convert('7 AM - 8 PM')

def test_time():
    with pytest.raises(ValueError):
        convert('6 AM - 14 PM')
    assert convert('1 AM to 7 AM') == '01:00 to 07:00'
    assert convert('10 AM to 2 PM') == '10:00 to 14:00'
    assert convert('1 PM to 5 AM') == '13:00 to 05:00'

def test_wrong_hour_or_minute():
    with pytest.raises(ValueError):
        convert('20 PM - 24 PM')
    with pytest.raises(ValueError):
        convert('10:60 AM to 12:70 PM')

if __name__ == "__main__":
    main()