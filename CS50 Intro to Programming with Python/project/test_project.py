from project import get_acknowledge, get_priority, get_task, get_time

def test_acknowledge():
    assert get_acknowledge("1") == True
    assert get_acknowledge("0") == False
    assert get_acknowledge(1) == "unknown"
    assert get_acknowledge("anything") == "unknown"

def test_priority():
    assert get_priority("1") == 1
    assert get_priority("0") == "nothing"

def test_task():
    assert get_task("Test 1") == "Test 1"
    assert get_task("Apples") == "Apples"
    assert get_task("0") == "nothing"

def test_time():
    assert get_time("12:30") == "12:30"
    assert get_time("2:30") == "02:30"
    assert get_time("32") == "00:32"
    assert get_time("") == "00:00"
    assert get_time("0") == "nothing"

def main():
    test_acknowledge()
    test_priority()
    test_task()
    test_time()

if __name__ == "__main__":
    main()