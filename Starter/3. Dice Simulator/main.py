import random

def dice(number: int):
    dice_lst = [1, 2, 3, 4, 5, 6]   # store as integers instead of strings
    rolls = [random.choice(dice_lst) for _ in range(number)]  # roll the dice
    print("You rolled:", ", ".join(map(str, rolls)))  # show dice results
    print("Total sum:", sum(rolls))  # show sum of rolls

def main():
    while True:
        try:
            dice_number = int(input("How many dice would you like to roll? "))
        except ValueError:
            print("Please key in a number")
            continue
        dice(dice_number)
        break

while True:
    main()
    play_again = input("Would you still want to continue?. y/n ").strip().lower()
    if play_again != "y":
        print("Thanks for playing")
        break
