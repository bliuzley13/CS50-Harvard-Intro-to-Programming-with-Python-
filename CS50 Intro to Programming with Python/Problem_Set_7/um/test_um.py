from um import count
import pytest

def main():
    test_um()

def test_um():
    assert count("Um") == 1
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("um, hello, um, world") == 2
    assert count("yummy") == 0
    assert count("hello, um, world") == 1


if __name__ == "__main__":
    main()