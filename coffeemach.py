from typing import Any

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO Check resources sufficient?
def resources_sufficient(drink_requirements):
    for ingredient in drink_requirements:
        if resources[ingredient] < drink_requirements[ingredient]:
            print(f"sorry you dont have enough {ingredient}")
            return False
    return True

# TODO process coins
def process_coins():
    print("please insert coins")
    quarter = int(input("How many quarters: $")) * 0.25
    dimes   = int(input("How many dimes: $"))* 0.10
    nickel  = int(input("How many nickel: $"))* 0.05
    penny   = int(input("How many pennies: $"))* 0.01
    total = quarter + dimes + nickel + penny
    return total

# TODO Check transaction successful?
def check_transaction(money_received,cost):
   if money_received >= cost:
       change = round(money_received - cost)
       print(f"here is your change ${change}")
       global money
       money += cost
       return True
   else:
       print("Sorry not enough money")
       return False

def make_coffee(drink_name , order_items):
    for items in order_items:
        resources[items] -= order_items[items]
    print(f"here is your {drink_name}☕ Enjoy!!")
 # TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# TODO Turn off the Coffee Machine by entering  "off” to the prompt
# TODO Print report


coffee_on = True
while coffee_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("off")
        coffee_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {money}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])





























