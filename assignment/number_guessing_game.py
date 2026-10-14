import random
#Importing random and setting lower and higher boundaries for an array function to get number from(in this case 1 and 100)
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

while is_running: # Constructing a loop that runs until the user guesses the correct number
    guess = input("Enter your guess:")
    if guess.isdigit(): #input the guess and check if it is digit(if not ask to enter again: lines 27-28)
        guess = int(guess)
        guesses+=1 #incrementing guesses 
        #logic so that user gets closer to the number with each try
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}") #After finding correct answer, telling that it was correct, printing in how many guesses the user got it, and turning is_running to False so that while loop breaks
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
