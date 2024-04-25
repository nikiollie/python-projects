import random

#generate random number
randNum = random.randint(1,100)

#print instructions
print("Guess a number between 1 and 100!")

#initialize guess
guess = 0

#continue to ask user to guess until guess is correct
while randNum != guess:
    
    #prompt user for guess (re-assign guess variable each time)
    guess = input("Input a guess: ")
    
    #guess will be string (input returns string), need to cast it 
    #  to int for comparison
    guess = int(guess)
    
    #compare user guess to random number
    if randNum > guess:
        print("Higher")
    elif randNum < guess:
        print("Lower")
    else:
        print("you guessed it")
    
