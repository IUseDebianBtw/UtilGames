import random

def roulette():
    # Simulate the spinning of the roulette wheel
    number = random.randint(0, 36)
    
    # Odd numbers are red, even numbers are black
    color = "Red" if number % 2 != 0 else "Black"
    
    # Special case for zero
    if number == 0:
        color = "Green"
    
    return number, color

def play_roulette():
    print("Welcome to Roulette!")
    while True:
        user_number = int(input("\nEnter your number (0-36): "))
        while user_number < 0 or user_number > 36:
            print("Invalid number. Please enter a number between 0 and 36.")
            user_number = int(input("\nEnter your number (0-36): "))

        print("The wheel is spinning...")
        number, color = roulette()
        print(f"The ball lands on {color} {number}!")

        if user_number == number:
            print("Congratulations! You win!")
        else:
            print("Sorry, better luck next time.")
        
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() not in ("yes","y"):
            break

play_roulette()
