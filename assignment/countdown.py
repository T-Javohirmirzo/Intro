import time #Importing the time module to handle execution delays
import math #Importing the math module to use math.floor() for rounding down

my_time = int(input("Enter the time in seconds: ")) # Getting the totak countdown time from user

if(my_time>0): #Ensure entered time is bigger than zero
    for x in range (my_time, 0, -1):
        #Calculate remaining hours, minutes, and seconds, then pause for 1 second
        print(f"{math.floor(x/3600)} hours: {math.floor((x % 3600) / 60)} minutes: {x%60} seconds")
        time.sleep(1)
    print("Time's up")
else:
    print("Time cannot be negative")