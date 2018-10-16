"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys

def start_game():
    # variables outside loop
    times_played = 0
    high_score = [""]

    # numbers game welcome menu
    welcome = "Welcome to the Numbers Guessing Game!"
    border = "-" * len(welcome)
    print(border)
    print(welcome)
    print(border)
    user_name = input("Please Enter your Name: ")

    #opening Loop
    while True:
        play_game = input("Would you like to play? Yes / No ")

        while True:
            if play_game.lower() == "no":
                print("\n" + border)
                print(" " * (10-len(user_name)) + "Thanks for Playing {}!".format(user_name))
                print(border)
                sys.exit()
            elif play_game.lower() == "yes":
                print("\n" + border)
                print(" " * (12-len(user_name)) + "Time to Play {}!".format(user_name))
                print(border)
                print

                # variables specific to each round
                answer = random.randint(0,10)
                guess_number = 1
                guess_attempts = []
                times_played += 1

                while True:
                    try:
                        print("*** Guess the Number between 1 and 10 ***")
                        if len(guess_attempts) > 0:
                                print("Numbers Guessed so far: " + ", ".join(guess_attempts))
                        guess = int(input("Please Enter your Guess  1 - 10 "))

                        # if guess is integer but outside range
                        if guess > 10 or guess < 0:
                            print("\n** The Number Guessed is not in Range **\n")

                        else:
                            # user guesses correctly
                            if guess == answer:
                                if guess_number == 1:
                                    print("\n** Amazing {}! You Guessed it in 1 try!!!! **\n".format(user_name))
                                else:
                                    print("\n** Congrats {}! You Guessed it in {} tries!! **\n".format(user_name, guess_number))

                                if times_played == 1:
                                    high_score[0] = guess_number
                                    if guess_number == 1:
                                        print("** You Set the High Score with {} attempt**\n".format(guess_number))
                                    else:
                                        print("** You Set the High Score with {} attempts**\n".format(guess_number))
                                else:
                                    if guess_number < high_score[0]:
                                        high_score[0] = guess_number
                                        if guess_number == 1:
                                            print("** You Set a New Record with {} try **\n".format(guess_number))
                                        else:
                                            print("** You Set a New Record with {} tries **\n".format(guess_number))
                                    else:
                                        print("***** Your High Score is still {} *****\n".format(high_score[0]))

                                play_game = input("Would you like to play again {}? Yes / No ".format(user_name))
                                break

                            #user guesses above answer
                            elif guess > answer:
                                print(border)
                                print("\n**** The Answer is Lower than {} ****\n".format(guess))
                                print(border)
                                print()
                                guess_attempts.append(str(guess))
                                guess_number += 1

                            #user guesses below answer
                            else:
                                print(border)
                                print("\n**** The Answer is Higher than {} ****\n".format(guess))
                                print(border)
                                print()
                                guess_attempts.append(str(guess))
                                guess_number += 1

                    #non-interger entered
                    except:
                        print("*** Please Enter a Valid Number ***")

            #yes or no not entered on play prompt
            else:
                print("\nPlease Enter Yes or No\n")
                break

if __name__ == '__main__':
    start_game()
