import random

def play_game():
    # Difficulty selection
    print("\n🎮 Choose difficulty level:")
    print("1. Easy   (1–10, 3 attempts)")
    print("2. Medium (1–50, 5 attempts)")
    print("3. Hard   (1–100, 7 attempts)")

    while True:
        choice = input("Select 1, 2, or 3: ").strip()
        if choice == "1":
            max_num, attempts = 10, 3
            break
        elif choice == "2":
            max_num, attempts = 50, 5
            break
        elif choice == "3":
            max_num, attempts = 100, 7
            break
        else:
            print("❌ Invalid choice, please select 1, 2, or 3.")

    number_to_guess = random.randint(1, max_num)
    print(f"\n🎲 Guess the number between 1 and {max_num}.")

    while attempts > 0:
        try:
            user_guess = int(input(f"👉 Your guess (Attempts left: {attempts}): "))
        except ValueError:
            print("❌ Please key in a valid number.")
            continue

        if user_guess == number_to_guess:
            print("🎉 Congrats, you guessed it correctly!")
            return True   # player won
        elif user_guess < number_to_guess:
            attempts -= 1
            print("📉 Too low. Try higher.")
        else:
            attempts -= 1
            print("📈 Too high. Try lower.")

    print(f"😢 No Luck. The number was {number_to_guess}.")
    return False  # player lost


# Scoreboard
wins, losses = 0, 0

# Main game loop
while True:
    if play_game():
        wins += 1
    else:
        losses += 1

    print(f"\n📊 Scoreboard: {wins} Wins | {losses} Losses")

    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("👋 Thanks for playing! Goodbye.")
        break
