import checks
import operator

valid_operators = ["+", "-", "*", "/"]
op = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}

app_quit = False

while not app_quit:
    i = checks.userInput()
    k = checks.operatorCheck(valid_operators, i[2])
    if k:
        try:
            op[i[2]](i[0], i[1])
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            print(op[i[2]](i[0], i[1]))
    else:
        print("Please enter a valid operator")
    app_quit = checks.userQuit()

