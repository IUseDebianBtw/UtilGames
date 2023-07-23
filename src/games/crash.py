import random
import time

def crash_game():
    print("Welcome to the crash game!")
    
    while True:
        bet = float(input("Enter your bet: "))
        cash_out_multiplier = float(input("Enter your cash out multiplier: "))

        multiplier = 1.0
        while True:
            # Game crashes randomly, but will always be at least 1.00x
            crash_point = random.uniform(1.0, 2.0)
            if crash_point < multiplier:
                print(f"Game crashed at {multiplier:.2f}x")
                print("You lost your bet.")
                break
            elif multiplier >= cash_out_multiplier:
                print(f"You cashed out at {multiplier:.2f}x")
                print(f"You won {bet * multiplier:.2f}")
                break
            else:
                multiplier += 0.01
                print(f"Current multiplier: {multiplier:.2f}x")
                time.sleep(0.1)  # Slow down the game a bit

        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() != "y":
            break

crash_game()
