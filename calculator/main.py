import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    print(n1 / n2)


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    print(art.logo)
    should_continue = True
    n1 = float(input("What is the first number?: \n"))

    while should_continue:

        for symbol in operations:
            print(symbol)
        operator_symbol = input("Pick an operation: ")
        n2 = float(input("What is the second number?: \n"))

        answer = operations[operator_symbol](n1, n2)

        print(f"{n1} {operator_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation\n")

        if choice == "y":
            n1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()