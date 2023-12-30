from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(7)
    assert jar2.capacity == 7

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(8)
    assert jar.size == 10

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5
