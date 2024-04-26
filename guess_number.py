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
    try:
        guess = int(guess)
    except:
        print("Not an integer!")
        continue
    
    #check for outlier
    if guess > 100 or guess < 1:
        print("Guess is out of range. Please guess a number between 1 and 100")
        continue

    #compare user guess to random number
    if randNum > guess:
        print("Higher")
    elif randNum < guess:
        print("Lower")
    else:
        print("You guessed it!")
    
