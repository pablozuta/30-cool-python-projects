import time
from playsound import playsound




def alarm(seconds):
    time_elapsed = 0
    

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60 # give us the remainder

        print(f"Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") # :02d formatea el codigo en dos digitos
    playsound("Alarm.wav")

minutes = int( input("How many minutes to wait: "))
seconds = int( input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)    
