import random
import hangman_words
from hangman_art import stages

lives=6


choose_word=random.choice(hangman_words.word_list)

placeholder=""
length=len(choose_word)
for dash in range(length):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letter=[]

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************************")
    guess = input("Guess the letter:").lower()

    if guess in correct_letter:
        print(f"You have already guess the {guess} letter")

    display=""
    
    for letter in choose_word:
        if letter==guess:
            display+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"

    print(display)

    if guess not in choose_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives==0:
            game_over=True
            print(f"******************************* IT WAS {choose_word}! YOU LOSE ******************************")
    
    if "_" not in display:
        game_over=True
        print("You Won")

    print(stages[lives])