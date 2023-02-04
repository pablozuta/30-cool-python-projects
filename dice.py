'''
As one of the most relatable Python projects for beginners with code, this program simulates rolling one or two dice. It’s also a great way to solidify your understanding of user-defined functions, loops, and conditional statements.

It uses the Python random module to replicate the random nature of rolling dice. Also it uses the os module to clear the screen after you’ve rolled the dice.
'''
import random
import os

def num_die():
    while True:
        try:
            num_dice = input('Number of dice: ')
            valid_responses = ['1', 'one', 'two', '2']
            if num_dice not in valid_responses:
                raise ValueError('Please choose 1 and 2 only')
            else:
                return num_dice
        except ValueError as err:
            print(err)    

def roll_dice():
    min_val = 1
    max_value = 6
    roll_again = 'y'

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_die()

        if amount == '2' or amount == 'two':
            print('Rolling the mf dice baby...')
            dice_1 = random.randint(min_val, max_value)
            dice_2 = random.randint(min_val, max_value)

            print('The values are:')
            print('Dice one: ', dice_1)
            print('Dice two: ', dice_2)
            print('Total: ', dice_1 + dice_2)

            roll_again = input('Roll again dude? ')
        else:
             print('Rolling the mf dice baby...')
             dice_1 = random.randint(min_val, max_value)
             print(f'The value is: {dice_1}')

             roll_again = input('Roll Again? ')

 
if __name__ == '__main__':
   roll_dice()