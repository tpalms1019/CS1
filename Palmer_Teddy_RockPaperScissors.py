 ,'''
Author: Teddy Palmer
Date: 12/1/23
Description: The code below allows the user to play rock paper scissors against a bot or a friend.
Challenges: Choose between playing multiplayer or against a bot, keeps track of score and declares winner, doesn't allow for user error on inputs (EX: input was not an available option, answer contained capitals, etc), uses tupples as a way to check for winning pairs, tracks win percentage verse the bot, uses sys.exit, keeps track of total games played, uses f strings for efficiency when using variable data in text, has very very basic anti cheat by printing 49 line breaks
Bugs: None
Sources: Ms. Marciano, Mr. Abanto
'''

import random # brings in the random library for reference
import sys # brings in the sys library for reference

rps = ["rock", "paper", "scissors"] # creates list of possible choices for the game rps
wins = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")] # creates list of tupples of winning matchups

score_user = 0 # creates a variable to keep track of the user's score
score_bot = 0 # creates a variable to keep track of the bot's score
score_user2 = 0 # creates a variable to keep track of the user two's score
games_played = 0 # creates a variable to keep track of the total games played


while True: # infinite loop while condition True is true
    play = str.lower(input("Want to play Rock Paper Scissors? ")) # sets play as a variable equal to the response of the question and converts answer to lowercase

    if play == "yes": # if play is yes, following code will happen
        print("awesome. ") # displays text depending on if if statement happens

        while True: # infinite loop while condition True is true
            multiplayer = str.lower(input("Do you want to play multiplayer? ")) # sets multiplayer as a variable equal to the response of the question and converts answer to lowercase

            if multiplayer == "yes": # if multiplayer is yes, following code will happen
                print("Great! ") # displays text depending on if if statement happens
                
                while True: # infinite loop while condition True is true
                    
                    while True: # infinite loop while condition True is true
                        user_rps = str.lower(input("Ok, player 1. pick 'rock', 'paper', or 'scissors'. Don't cheat. It'll ruin the fun. ")) # sets user_rps as a variable equal to the response of the question and converts answer to lowercase

                        if user_rps in rps: # if user_rps is one of the elements of the list rps
                            break # then manually break while loop
                        else: # otherwise
                            print("Invalid please enter 'rock', 'paper', or 'scissors' ") # display text

                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # displays 49 enters so that user 2 cannot see user's input


                    while True:  # infinite loop while condition True is true
                        user2_rps = str.lower(input("Ok, now player 2. pick 'rock', 'paper', or 'scissors'. Don't cheat. It'll ruin the fun. ")) # sets user2_rps as a variable equal to the response of the question and converts answer to lowercase

                        if user2_rps in rps: # if user2_rps is one of the elements of the list rps 
                            break # then manually break while loop
                        else: # otherwise
                            print("Invalid please enter 'rock', 'paper', or 'scissors' ") # display text
             
                    games_played += 1 # then add 1 to variable games_played

                    if (user_rps, user2_rps) in wins: # if the user bot pair is in the list of winning pairs
                        print("Player 1 wins! ")  # then display text
                        score_user += 1 # adds 1 to variable score_user
                    elif user_rps == user2_rps: # if user_rps equals bot_rps
                        print("It's a tie ") # then display text                       
                    else: # otherwise
                        print("Player 2 wins ") # display text
                        score_user2 += 1 # add 1 to variable score_bot

                    while True: # infinite loop while condition True is true
                        play_again = str.lower(input(f"You have played {games_played} game(s). Do you want to play again? ")) # sets play_again as a variable equal to the response of the question and converts answer to lowercase

                        if play_again == "yes": # if play_again is yes, following code will happen
                            print("Awesome. ") # displays text depending on if if statement happens
                            print(f"Player 1: {score_user} - Player 2: {score_user2} ") # uses an f string to cocatenate different variable data types as a single string
                            break # manually breaks while loop
                        elif play_again == "no": # if play_again is no, following code will happen
                            print(f"The final score was Player 1: {score_user} - Player 2: {score_user2} ") # displays both players and their scores

                            if score_user > score_user2: # if score_user is greater than score_user2
                                print("Player 1 wins! ") # then display text depending on if if statement happens
                                sys.exit() # directly ends the code
                            elif score_user < score_user2: # if score_user is less than score_user2, following code will happen
                                print("Player 2 wins! ") # displays text depending on if elif statement happens
                                sys.exit() # directly ends the code
                            else: # otherwise, if score_user is not greater than or less than score_user2, following code will happen
                                print("Both players tied. It is a draw. ") # displays text depending on if else statement happens
                                sys.exit() # directly ends the code
                        else: # if play_again is not yes or no, following code will happen
                            print("Invalid. Please answer with 'yes' or 'no' ") # displays text depending on if else statement happens
            elif multiplayer == "no": # if multiplayer is no, following code will happen
                print("Great! You will be playing a bot. ")  # if multiplayer is no, following code will happen
                
                while True: # infinite loop while condition True is true

                    bot_rps = random.choice(rps) # sets bot_rps as a variable equal to a random element of the list rps
                    
                    while True: # infinite loop while condition True is true
                        user_rps = str.lower(input("Ok. pick 'rock', 'paper', or 'scissors'.  ")) # sets user_rps as a variable equal to the response of the question and converts answer to lowercase

                        if user_rps in rps: # if user_rps is one of the elements of the list rps
                            break # then manually break while loop
                        else: # otherwise
                            print("Invalid please enter 'rock', 'paper', or 'scissors' ") # display text

                    print(f"I chose {bot_rps}") # displays text and the variable bot_rps as a string
                    
                    games_played += 1 # adds 1 to the variable games_played
                    
                    if (user_rps, bot_rps) in wins: # if the user bot pair is in the list of winning pairs
                        print("Damn. You win. ")  # then display text
                        score_user += 1 # adds 1 to variable score_user
                    elif user_rps == bot_rps: # if user_rps equals bot_rps
                        print("It's a tie ") # then display text                       
                    else: # otherwise
                        print("Yes! I win. ") # display text
                        score_bot += 1 # add 1 to variable score_bot

                    while True: # infinite loop while condition True is true
                        play_again = str.lower(input(f"You have played {games_played} game(s). Do you want to play again? ")) # sets play_again as a variable equal to the response of the question and converts answer to lowercase                        
                            
                        percentage_winrate = (score_user/games_played)*100 # creates a variable to keep track of the percentage of games won verse the bot
                        if play_again == "yes":  # if play_again is yes, following code will happen
                            print("Awesome. ") # displays text depending on if if statement happens
                            print(f"user: {score_user} - bot: {score_bot} ") # displays both the player and bot's scores
                            print(f"You have won {percentage_winrate}% of the games ") # displays the percentage of games won
                            break # manually breaks while loop
                        elif play_again == "no":  # if play_again is no, following code will happen
                            print(f"You won {percentage_winrate}% of the games ") # displays the percentage of games won
                            print(f"user: {score_user} - bot: {score_bot} ") # displays both the player and bot's scores
                            if score_user > score_bot: # if score_user is greater than score_bot
                                print("Damn. You win. Well played.") # display text
                            elif score_user < score_bot: # if score_user is less than score_bot then
                                print("Yes! I win.") # display text
                            else: # If score_user is not greater than or less than score_bot then
                                print("It's a draw. Well played.") # display text
                            print("Have good day.") # displays text depending on if elif statement happens
                            sys.exit() # directly ends the code
                        else: # if play_again is not yes or no, following code will happen
                            print("Invalid. Please answer with 'yes' or 'no' ") # displays text depending on if else statement happens
        break # manually breaks while loop
    elif play == "no": # otherwise if play is no
        print("ok then why are you here. Get out. ") # displays text depending on if elif statement happens
        break # manually breaks while loop
    else: # if play is not one of the above options then this code happens
        print("Invalid. 'yes' or 'no' answer please.") # displays text depending on if else statement happens


