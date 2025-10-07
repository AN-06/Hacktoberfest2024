# lottery_game.py

import random
import time

def lottery_game():
    print("🎰 Welcome to the Python Lottery Game! 🎰")
    print("Pick a number between 1 and 10.")
    
    try:
        user_num = int(input("Enter your number: "))
        if user_num < 1 or user_num > 10:
            print("❌ Please choose a number between 1 and 10.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return
    
    print("\nDrawing 3 random numbers...")
    time.sleep(1)
    
    winning_numbers = random.sample(range(1, 11), 3)
    print(f"🎲 Winning numbers are: {winning_numbers}")
    
    if user_num in winning_numbers:
        print("🎉 Congratulations! You WON the lottery!")
    else:
        print("😔 Better luck next time!")

if __name__ == "__main__":
    lottery_game()
