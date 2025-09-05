def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

operation = {
    "+": add,
    "-":subtract,
    "*": multiply,
    "/":division,
}
def calculator():
    import calc_art
    print(calc_art.logo)
    should_continue = True
    first_number = float(input("Enter the first number: "))
    while should_continue:
        for symbols in operation:
            print(symbols)
        oper = input("Choose an operator: ")
        second_num = float(input("Enter the second number: "))
        answer = operation[oper](first_number,second_num)

        print(f"{first_number} {oper} {second_num} = {answer} ")

        choice = input("Type 'y' to continue calculating with the number or type 'n' to start a new calculator: ").lower()

        if choice == "y":
            first_number = answer
        elif choice == "n":
            should_continue = False
            print("\n"*20)
            calculator()

calculator()