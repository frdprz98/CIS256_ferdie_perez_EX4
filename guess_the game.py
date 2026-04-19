# Import random so we can choose a random word
import random

# Predefined list
word_list = ["tape", "wire", "panel", "screwdriver"]

# Function: choose random word
def choose_word():
    return random.choice(word_list)

# Function: process one guess
def process_guess(secret_word, guess, word):
    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if letter == guess:
                word[index] = guess
        return "correct"
    else:
        return "incorrect"


# Main game
if __name__ == "__main__":

    # Choose one random word from the list
    secret_word = choose_word()

    # Game settings
    attempts = 9
    guesses = []
    word = ["_"] * len(secret_word)

    # Welcome message
    print("Guess the word")
    print("Press a letter to begin")
    print("You have", attempts, "incorrect attempts.\n")

    # Game loop
    while attempts > 0 and "_" in word:

        # Show current progress
        print("Word:", " ".join(word))
        print("Guessed letters:", guesses)

        # Ask the user for one letter
        guess = input("Enter one letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE letter.\n")
            continue

        # Check if letter was already guessed
        if guess in guesses:
            print("You already guessed that letter.\n")
            continue

        # Save guessed letter
        guesses.append(guess)

        # Check guess
        result = process_guess(secret_word, guess, word)

        if result == "correct":
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")
            print("Attempts left:", attempts)

        print()

    # End of game results
    if "_" not in word:
        print("Congratulations! You guessed the word:", secret_word)
    else:
        print("Game Over!")
        print("The word was:", secret_word)
