import random

# Symbols on the slot machine
SYMBOLS = ["1", "2", "3", "4", "5", "6", "8", "9"]

def spin_reels():
    """
    Spins the slot machine reels and returns the result.
    """
    return random.choices(SYMBOLS, k=3)

def check_win(reels):
    """
    Checks if the spin resulted in a win.
    """
    return len(set(reels)) == 1

def slot_machine():
    print("Welcome to the slot machine!")
    while True:  # Play until the user decides to stop
        print("Spinning the reels...")
        reels = spin_reels()
        print(" ".join(reels))
        if check_win(reels):
            print(f"Congratulations, you got 3 {reels[0]}s! You win!")
        else:
            print("Sorry, better luck next time.")
        
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() not in ("yes","y"):
            break
        print()

slot_machine()
