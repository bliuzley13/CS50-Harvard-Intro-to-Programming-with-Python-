from fuel import convert, gauge
import pytest

def main():
    test_0DivError()
    test_ValError()
    test_Correct()

def test_0DivError():
    with pytest.raises(ZeroDivisionError):
        convert ('5 / 0')

def test_ValError():
    with pytest.raises(ValueError):
        convert ('cat/5')

def test_Correct():
    assert convert('1/100') == 1 and gauge(1) == "E"
    assert convert('1/1') == 100 and gauge(100) == "F"
    assert convert('99/100') == 99 and gauge(99) == "F"
    assert convert('50/100') == 50 and gauge(50) == "50%"

if __name__ == "__main__":
        main()