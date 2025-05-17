def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are paths to the north and east.")
    first_choice()

def first_choice():
    choice = input("Do you go north or east? ").strip().lower()
    if choice == "north":
        cave()
    elif choice == "east":
        river()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def cave():
    print("\nYou arrive at a cave. It's dark and you hear strange noises.")
    choice = input("Do you enter the cave or go back? ").strip().lower()
    if choice == "enter":
        print("You bravely enter the cave and find treasure. You win!")
    elif choice == "go back":
        first_choice()
    else:
        print("Invalid choice. Try again.")
        cave()

def river():
    print("\nYou reach a river. The current looks strong.")
    choice = input("Do you swim across or build a raft? ").strip().lower()
    if choice == "swim":
        print("The current is too strong. You are swept away. Game over.")
    elif choice == "build a raft":
        print("You build a raft and safely cross the river. You find a village. You win!")
    else:
        print("Invalid choice. Try again.")
        river()

if __name__ == "__main__":
    intro()
