from seasons import checkValid, ageMinWords
import pytest

#These tests work only in regards to the current day which is today
def main():
    test_days()
    test_months()
    test_years()

def test_days():
    assert checkValid('2023-08-16') == 1
    assert checkValid('2023-08-15') == 2
    with pytest.raises(ValueError):
        ageMinWords('2023-8-16')
    with pytest.raises(ValueError):
        ageMinWords('August 16, 2023')

def test_months():
    assert checkValid('2023-07-17') == 31
    assert checkValid('2023-06-17') == 61

def test_years():
    assert checkValid('2022-08-17') == 365
    assert checkValid('2021-08-17') == 730

if __name__ == "__main__":
    main()