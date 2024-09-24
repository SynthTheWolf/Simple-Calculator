def operatorCheck(valid_operators, c):
    for i in range(len(valid_operators)):
        if valid_operators[i] == c:
            return True
            break
        elif i < len(valid_operators) - 1:
            continue
        else:
            return False

def userInput():
    while True:
        try:
            a = float(input("Please enter the 1st value: "))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    while True:
        try:
            b = float(input("Please enter the 2nd value: "))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    c = input("Please enter a valid operator (+-*/): ")
    return [a, b, c]

def userQuit():
    q = input("Do you want to quit y/n: ")
    try:
        q == "y" or q == "n"
    except ValueError:
        print("Please enter a valid input")
    finally:
        if q == "y":
            return True
        else:
            return False