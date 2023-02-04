'''
This  countdown timer asks the user for a number of seconds via user input, and it then counts down, second by second, until it displays a message.

We’ve used the Python time module’s .sleep() function to pause for 1-second intervals. We combine this with some nifty string formatting to produce the countdown display.

'''
import time

def countdown(user_time):
    while user_time >= 0:
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        user_time -= 1
    print('List off!')

if __name__ == '__main__':
    user_time = int(input('Enter a time in seconds: '))
    countdown(user_time)        