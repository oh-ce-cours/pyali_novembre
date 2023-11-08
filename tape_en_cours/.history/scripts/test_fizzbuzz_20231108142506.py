import fizzbuzz


def test_fizzbuzz_1_fizz():
    assert fizzbuzz.fizzbuzz_1_for_number(3) == "fizz"


def test_fizzbuzz_1_buzz():
    assert fizzbuzz.fizzbuzz_1_for_number(5) == "buzz"


def test_fizzbuzz_1_fizzbuzz():
    assert fizzbuzz.fizzbuzz_1_for_number(15) == "fizzbuzz"


def test_fizzbuzz_1_nombres():
    assert fizzbuzz.fizzbuzz_1_for_number(4) == "4"
