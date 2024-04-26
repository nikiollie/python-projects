import random

def game():

    print("Rock, paper, or scissors. Best of three! Good luck!")
   
    while True:
        game_options = input("Do you want ties to count towards the three rounds [y/n]? ")
        #confirm input is valid
        if game_options != "y" and game_options != "n":
            print("Invalid input!")
            continue

        count = 0
        scores = {"user": 0, "computer": 0}

        while count < 3:

            user = input("Rock, paper or scissors [r, p, s]? ")

            #confirm user input is valid
            if user != "r" and user != "p" and user != "s":
                print("Invalid input!")
                continue

            options = ["rock", "paper", "scissors"]
            comp_guess = random.choice(options)
            print("The computer chose " + comp_guess)

            #paper beats rock
            #rock beats scissors
            #scissors beats paper

            is_tie = False

            if user == "r":
                if comp_guess == "paper":
                    print("Computer wins!")
                    scores["computer"] += 1
                elif comp_guess == "scissors":
                    print("You win!")
                    scores["user"] += 1
                else:
                    print("It's a tie!")
                    is_tie = True
            elif user == "p":
                if comp_guess == "paper":
                    print("It's a tie!")
                    is_tie = True
                elif comp_guess == "scissors":
                    print("Computer wins!")
                    scores["computer"] += 1
                else:
                    print("You win!")
                    scores["user"] += 1
            else:
                if comp_guess == "paper":
                    print("You win!")
                    scores["user"] += 1
                elif comp_guess == "scissors":
                    print("It's a tie!")
                    is_tie = True
                else:
                    print("Computer wins!")
                    scores["computer"] += 1


            #increment count or not based on game options/if tie
            if game_options == "y":
                count += 1
            else:
                if is_tie == False:
                    count += 1

        # check who won
        print("Final score for this round.. user: " + str(scores["user"]) + ", computer: " + str(scores["computer"]))

        if scores["user"] > scores["computer"]:
            print("You won the game!")
        elif scores["user"] < scores["computer"]:
            print("The computer won the game!")
        else:
            print("It was a tied game!")

        #option to play again
        play_again = input("Do you want to play again [y/n]? ")
        if play_again == "y":
            continue
        else:
            print("Great game, bye!")
            break


if __name__ == "__main__":
    game()
