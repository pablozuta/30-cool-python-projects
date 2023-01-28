import random

attemps_list = []

def show_score():
    if not attemps_list:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print(f"The current high score is {min(attemps_list)} attemps") 

def start_game():
    attemps = 0
    rand_num = random.randint(1, 10)
    print("Hello traveler! Welcome to the game of guesses") 
    player_name = input("What is your name? ")
    wanna_play = input(
        f"Hi, {player_name}, would you like to play the guessing game?"
        "(Enter Yes/No): ")     

    if wanna_play.lower() != 'yes':
        print("That's fine")
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("number must be between 1 and 10")

            attemps += 1
            attemps_list.append(attemps)

            if guess == rand_num:
                print("Nice, You got it!")
                print(f"It took you {attemps} attemps")
                wanna_play = input(
                    "Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != 'yes':
                    print("That's cool , have a nice one")
                    break
                else:
                    attemps = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print("It is lower")
                elif guess < rand_num:
                    print("It is higher")

        except ValueError as err:
                print("That's not a valid value , try again :) ")
                print(err)

if __name__ == '__main__':
    start_game()


