print(f"(dans test_fizzbuzz.py avant import) {__name__ = }")
from scripts.fizzbuzz import fizzbuzz_1_for_number

print(f"(dans test_fizzbuzz.py apres import) {__name__ = }")


def test_fizzbuzz_1_fizz():
    assert fizzbuzz_1_for_number(3) == "fizz"


def test_fizzbuzz_1_buzz():
    assert fizzbuzz_1_for_number(5) == "buzz"


def test_fizzbuzz_1_fizzbuzz():
    assert fizzbuzz_1_for_number(15) == "fizzbuzz"


def test_fizzbuzz_1_nombres():
    assert fizzbuzz_1_for_number(4) == "4"
