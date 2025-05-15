#YouTube channel 5starcoder
#subscribe my channel 
#project_01
# Mad Libs Generator

print("Welcome to the Mad Libs Generator!")
print("You'll be asked for different words to create a funny story. Let's go!\n")

while True:
    # Asking the user for words
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose another noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (a describing word): ")
    noun3 = input("Choose one more noun: ")

    # Printing the final Mad Libs story
    print("\n------------------------------------------")
    print(f"Be kind to your {noun} - footed {p_noun}")
    print(f"For a duck may be somebody's {noun2},")
    print(f"Be kind to your {p_noun} in {place}")
    print(f"Where the weather is always {adjective}. \n")
    print(f"You may think that this is the {noun3},")
    print("Well, it is.")
    print("------------------------------------------")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
