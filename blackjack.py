import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "You lost, opponent has black blackjack"
    elif u_score == 0:
        return "You win by blackjack"
    elif c_score > 21:
        return "You LOST, went over"
    elif u_score > 21:
        return "You WON, opponent went over"
    elif u_score > c_score:
        return "You win"
    else:
        return "You Lose"


def play_game():
    print(logo)
    user_card=[]
    computer_card =[]
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate(user_card)
        computer_score = calculate(computer_card)
        print(f"Your cards: {user_card}, total score {user_score}")
        print(f"Your cards: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("type 'y' to get another card, or type 'n' ").lower()
            if choice == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate(computer_card)

    print(f"Your final card: {user_card}, your final score {user_score}")
    print(f"computers final hand: {computer_card}, final score {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of BLACKJACK type(Y or N): ").lower() == "y":
    print("\n"*20)
    play_game()



