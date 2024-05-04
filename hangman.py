from words import *
import random

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

word = random.choice(word_list)
guess_list = []
wrong_guess_list = []
word_dict = {}
wrong_guesses = 0
correct_guesses = 0
num_letters = len(word)

print("Guess the word, one letter at a time!")
for i in range(num_letters):
    word_dict[i] = ' '
    print("_", end="")

print("\n")

while wrong_guesses < 11 and correct_guesses != num_letters:
    if len(wrong_guess_list) >0:
        print("Wrong guesses so far: ")
    for i, ltr in enumerate(wrong_guess_list):
        print(ltr, end="")

    print("\n")

    guess = input("What is your guess: ")

    if guess in guess_list:
        print("Already guessed!")
        continue
    else:
        guess_list.append(guess)

        if guess in word:
            print("You guessed a letter")
            num_occurences = word.count(guess)
            correct_guesses += num_occurences
            index_list = find(word, guess)
    
            for index in index_list:
                word_dict[index] = guess
        else:
            print("Not in the word :(")
            wrong_guesses += 1
            wrong_guess_list.append(guess)
            print("You have " + str(11-wrong_guesses) + " guesses left.")
        
        #print pattern
        for i in range(num_letters):
            print(word_dict[i], end="")
        print("\n")
        for i in range(num_letters):
            print("_", end="")

        print("\n")

if correct_guesses == num_letters:
    print("You guessed the word " + word + " correctly!")
else:
    print("The word was " + word)
    print("Better luck next time!")

