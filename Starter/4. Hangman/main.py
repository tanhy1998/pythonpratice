import random

def run_game():
    player_name = input("What is your name? ")
    attempts = 6  # more realistic for Hangman
    print(f"Welcome to Hangman, {player_name}! Please guess the word.")

    words = ["secrets", "peixian", "hongyang"]
    guess_word = random.choice(words)

    # Start with all blanks
    guessed_lst = ["_"] * len(guess_word)

    # Keep track of wrong guesses
    wrong_guesses = []

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_lst))
        print(f"Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"Attempts left: {attempts}")

        guessed = input("Enter a letter: ").lower()

        if len(guessed) != 1 or not guessed.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guessed in guessed_lst or guessed in wrong_guesses:
            print("You already guessed that letter.")
            continue

        if guessed in guess_word:
            # Update guessed_lst where letters match
            for i, char in enumerate(guess_word):
                if char == guessed:
                    guessed_lst[i] = guessed
            print("Good guess!")
        else:
            wrong_guesses.append(guessed)
            attempts -= 1
            print("Wrong guess!")

        # Check if player has guessed the whole word
        if "_" not in guessed_lst:
            print("\n🎉 Congrats, you guessed the word:", guess_word)
            break
    else:
        print("\n❌ No more attempts! The word was:", guess_word)


if __name__ == "__main__":
    run_game()
