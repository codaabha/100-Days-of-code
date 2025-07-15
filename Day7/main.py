
#This is a work in progress for Hangman Project

#Day 7 project: Hangman
#Topic: Flowchart programming, picking random words/guess+checking answers
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
