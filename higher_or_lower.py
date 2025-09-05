# import the modules
import random
from art_hl import logo,vs
from higherlower_data import data

# make the value into a format
def convert_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_follower(user_guess ,a_follower,b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
# generate random value from list
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)


    if account_a == account_b:
        account_b = random.choice(data)

    # calling the format function
    print(f"Compare A : {convert_format(account_a)}")
    print(vs)
    print(f"Against : {convert_format(account_b)}")


    # ask the user input
    guess = input("Who has more followers(A or B): ").lower()

    print(logo)


    # get the follower count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #  check the user input

    check = check_follower(guess,a_follower_count,b_follower_count)

    # update the score
    if check:
        score += 1
        print(f"you are right, current score {score}")
    else:
        print("you are wrong")
        game_should_continue = False

# make the code repeatable

# comparing with the right answer
