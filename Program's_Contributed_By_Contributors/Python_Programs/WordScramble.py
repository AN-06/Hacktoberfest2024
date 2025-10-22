import random

def word_scramble():
    words = ["python", "developer", "hacktoberfest", "programming", "opensource"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    
    print("🔤 Unscramble the word!")
    print(f"Scrambled word: {scrambled}")
    guess = input("Your guess: ").lower()
    
    if guess == word:
        print("🎉 Correct! You unscrambled it right!")
    else:
        print(f"❌ Oops! The correct word was '{word}'.")

if __name__ == "__main__":
    word_scramble()
