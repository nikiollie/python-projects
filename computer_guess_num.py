import random

def ask_user():
    num = int(input("What is a number between 1 and 100? "))
    return num

def computer_guess(user_num):
    guess = 0

    min_guess = 1
    max_guess = 100

    while guess != user_num:

        guess = random.randint(min_guess, max_guess)
        
        if guess > user_num:
            print("Computer guess of " + str(guess) + " is wrong! The number is lower")
            max_guess = guess-1
        elif guess < user_num:
            print("Computer guess of " + str(guess) + " is wrong! The number is higher")
            min_guess = guess+1
        else:
            print("Computer guess of " + str(guess) + " is correct!")


if __name__ == "__main__":
    user_num = ask_user()
    computer_guess(user_num)
