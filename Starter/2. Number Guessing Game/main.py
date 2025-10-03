import random

def play_game():
    print("Guess the number between 1 and 10.")
    attempts = 3
    number_to_guess = random.randint(1, 10)

    while attempts > 0:
        try:
            user_guess = int(input(f"Please guess a number between 1 - 10. You have {attempts} attempts left: "))
        except ValueError:
            print("Please key in a correct number.")
            continue

        if user_guess == number_to_guess:
            print("🎉 Congrats, you guessed it correctly!")
            break
        elif user_guess < number_to_guess:
            attempts -= 1
            print(f"Too low. Try higher numbers. You have {attempts} left.")
        else:
            attempts -= 1
            print(f"Too high. Try lower numbers. You have {attempts} left.")

    else:
        print(f"😢 No Luck. The number was {number_to_guess}. Try again next time!")

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing")
        break


