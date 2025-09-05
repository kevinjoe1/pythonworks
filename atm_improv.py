from datetime import datetime


account_balance = 1000
PIN = "1234"
transaction_history =[]


def authenticate_user():
    """Authenticates user at the start of the session"""
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == PIN:
            print("Authentication successful")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"incorrect password, {attempts} remaining")
            else:
                print("Too many incorrect attempts session expired:")
    return False


def add_transaction(transaction_type,amount):
    """Adds transaction to history"""
    transaction = {
        "type" : transaction_type,
        "amount": amount,
        "balance_after": account_balance,
        "timestamp": datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
    }
    transaction_history.append(transaction)


def show_menu():
    """Display ATM menu options"""
    print(  "=" *35)
    print("          ATM MAIN MENU")
    print("="*35)

    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transaction History")
    print("5. Exit")
    print("=" *35)


def get_user_choice():
    """Get the user input"""
    while True:
        try:
            choice = int(input("Select an option form (1 - 5): "))
            if 1<= choice <=5:
                return choice
            else:
                print("please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

def check_balance():
    """Display current balance """
    print("\n---BALANCE INQUIRY----")
    print(f"Current Balance: ${account_balance:.2f}")
    add_transaction("Balance inquiry",0)

def withdraw_money():
    """Process money withdrawal """
    global account_balance
    print("\n----WITHDRAWAL----")
    print(f"Available Balance: ${account_balance:.2f}")

    while True:
        try:
            amount = float(input("How much money do you want to withdraw: $"))
            if amount <=0:
                print("Amount must be greater than zero.")
                continue
            if amount > account_balance:
                print(f"Insufficient bank balance: ${account_balance:.2f}")
                continue
            if amount %10 != 0:
                print("Please enter amount in multiples of $10")
                continue
            break
        except ValueError:
            print("Please enter a valid amount")


    account_balance -= amount
    add_transaction("Withdrawal",amount)
    print(f"${amount:.2f} withdrawn successfully")
    print(f"Account balance after: ${account_balance:2f}")

def deposit_money():
    """Process money deposit to account"""
    print("\n----DEPOSIT MONEY----")
    while True:
        try:
            amount = float(input("How much money do you want to deposit: $"))
            if amount <= 0:
                print("The amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    global account_balance
    account_balance += amount
    add_transaction("Deposit",amount)
    print(f"New bank balance : ${account_balance}")


def show_transaction_history():
    """Displays recent transactions"""
    print("\n----TRANSACTION HISTORY----")
    if not transaction_history:
        print("No transaction history yet")
        return
    print(f"{'Date/time':<23} {'Type':<16} {'Amount': <12} {'Balance': <12}")
    print("-"*62)

    for transaction in transaction_history:
        amount_str = f"{transaction['amount']:.2f}" if transaction['amount'] != 0 else "N/A"
        balance_str = f"{transaction['balance_after']:.2f}"
        print(f"{transaction['timestamp']:<20} {transaction['type']:<16} {amount_str:<12} {balance_str: <12}")

def main():
    """Main atm program"""
    print("🏧 WELCOME TO PYTHON ATM")
    print("-"*25)

    if not authenticate_user():
        return

    print(f"\nWelcome to day is {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    while True:
        show_menu()
        choice = get_user_choice()
        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw_money()
        elif choice == 3:
            deposit_money()
        elif choice == 4:
            show_transaction_history()
        elif choice == 5:
            print("Thank you for using python ATM🏧")
            print("Have a GREAT DAY! ")
            break

        input("\nPress enter to continue.....")

if __name__ == "__main__":
    main()


