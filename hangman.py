import random

from hngman_list import word_list
from projects.hngman_art import logo,stages

lives = 6
print(logo)

choice_word = random.choice(word_list)
print(choice_word)

placeholder=""
for letter in choice_word:
    placeholder +="_"
print(placeholder)

game_over = False
game_list = []
while not game_over:
    print(f"**********************({lives}/6)left*************************")
    guess = input("Guess a letter: ").lower()

    if guess in game_list:
        print(f"you've already guessed the word{guess}")

    display = ""

    for letter in choice_word:
        if letter == guess:
            display+=letter
            game_list.append(letter)
        elif letter in game_list:
            display += letter
        else:
            display+="_"

    print("word to Guess: ",display)

    if guess not in choice_word:
        lives -= 1
        print(f" You guessed the wrong word it was: {guess}")

        if guess == 0:
            print("******************** You LOST *******************")
            game_over = True




    if "_" not in display:
        game_over = True
        print("******************* You WON *********************")


    print(stages[lives])















