# Author: Mongezi Nene
# Student number: 215026717
# Description: this program reads in a value and the computer makes a choice randomly and these values are used to play rock, paper, scissors then outputs the winner

import random # import random so random funtion can be used

print("***A game of rock paper scissors between you and the computer.*** \n***See how many times you can win.*** \n***Play as many rounds as you desire.*** \n") # prints that user will be playing rock paper scissors
print("**Rules: Your choice must be an integer from 1 to 3 otherwise the Computer wins the round by default.**\n*Let the games begin.*\n") # prints the rules of the game

# initial number of wins

player_wins = 0
comp_wins = 0

x = int(input("Enter how many rounds you would like to play :")) # input the number of rounds to be played

# selection statement for no rounds played
if x == 0:
    print("\nNo round played.")


# loop for however many round user wants to be played
else:
    for i in range(x):
        print("\nRound:", i + 1) # prints what round is being played
        comp_hand = random.randint(1,3) # computer chooses a value randomly
        player_hand = int(input("\nRock(1), Paper(2) or Scissors(3) :")) # user inputs their choice
        
        # selection statement for an invalid input
        if player_hand < 1 or player_hand > 3:
            print("\nInvalid input.\nComputer wins this round by default.") # prints that input was invalid
            comp_wins = comp_wins + 1 # penalty for entering an invalid input
        
        # selection statement for when it's a tie
        elif comp_hand == player_hand: 
            if comp_hand == 1:
                print("\nComputer chose Rock") # prints that computer chose rock
                print("It's a tie. Both chose Rock") # print statement for when computer both choose rock
            elif comp_hand == 2:
                print("\nComputer chose Paper") # prints that computer chose paper
                print("It's a tie. Both chose Paper") # print statement for when computer both choose paper
            else:
                print("\nComputer chose Scissors") # prints that computer chose scissors
                print("It's a tie. Both chose Scissors") # print statement for when computer both choose scissors
                
        # selection statement for when user wins    
        elif comp_hand == 1 and player_hand == 2 or comp_hand == 2 and player_hand == 3 or comp_hand == 3 and player_hand == 1: 
            if player_hand == 1:
                print("\nComputer chose Scissors")
                print("You win. Rock beats Scissors")
            elif player_hand == 2:
                print("\nComputer chose Rock")            
                print("You win. Paper beats Rock")
            else:
                print("\nComputer chose Paper")
                print("You win. Scissors beats Paper")
            player_wins = player_wins + 1 # adds one win if the player wins a round
            
        # selection statement for when computer wins
        else: 
            if comp_hand == 1:
                print("\nComputer chose Rock")            
                print("You lose. Rock beats Scissors")
            elif comp_hand == 2:
                print("\nComputer chose Paper")            
                print("You lose. Paper beat Rock")
            else:
                print("\nComputer chose Scissors")            
                print("You lose. Scissors beats Paper")
            comp_wins = comp_wins + 1 # adds one win if the computer wins a round
            
     # selection statements for the number of rounds won
    if comp_wins == 1:
        print("\nComputer won", comp_wins, "round out of", x) # prints that computer won a round
    else:
        print("\nComputer won", comp_wins, "rounds out of", x) # prints number of rounds won by the computer
    if player_wins == 1:
        print("\nYou won", player_wins, "round out of", x) # prints that player won a round
    else:
        print("\nYou won", player_wins, "rounds out of", x) # prints number of rounds won by the player    