print(2 + 2)
a = 2
a = a + "2"

a = 1
b = 2
match a, b:
    case 0, 0:
        print("1")
    case 1, 1:
        print("2")
    case 1, 2:
        print("3")
    case _, _:
        print("toto")
