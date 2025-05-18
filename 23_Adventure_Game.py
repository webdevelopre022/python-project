def intro():
    print("You wake up in a dark forest. There are two paths ahead.")
    print("Do you go left or right?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        intro()

def left_path():
    print("\nYou walk down the left path and find a river.")
    print("Do you try to swim across or walk along the riverbank?")
    choice = input("Type 'swim' or 'walk': ").lower()
    if choice == "swim":
        print("\nThe current is too strong! You are swept away. Game Over.")
    elif choice == "walk":
        print("\nYou find a bridge and cross safely. You win!")
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("\nYou take the right path and encounter a hungry wolf.")
    print("Do you run or try to scare it away?")
    choice = input("Type 'run' or 'scare': ").lower()
    if choice == "run":
        print("\nYou escape safely into a nearby cave. You win!")
    elif choice == "scare":
        print("\nThe wolf is not impressed. Game Over.")
    else:
        print("Invalid choice. Try again.")
        right_path()

if __name__ == "__main__":
    intro()
