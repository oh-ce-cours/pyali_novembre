print(2 + 2)

A = 2
b = 2
match A, b:
    case 0, 0:
        print("1")
    case 1, 1:
        print("2")
    case 1, 2:
        print("3")
    case _, _:
        print("toto")
