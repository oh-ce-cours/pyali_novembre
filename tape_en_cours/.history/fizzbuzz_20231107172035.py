def fizzbuzz_1():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


for number in range(1, 101):
    res = ""
    if number % 3 == 0:
        res += "fizz"
    if number % 5 == 0:
        res += "buzz"
    if number % 7 == 0:
        res += "bazz"
    if not res:
        res = str(number)

    print(res)
