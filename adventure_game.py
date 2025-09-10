def get_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print("\nInvalid choice. Try again.")

def replay_prompt():
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    return replay == "yes"

def start_game():
    print("\nWelcome to the Adventure Game!")
    name = input("What is your name, brave explorer? ")
    print(f"\nHello {name}! Your quest is to find the legendary treasure.")
    print("You stand at a crossroads. Do you want to:")
    print("1. Explore the dark forest 🌲")
    print("2. Enter the mysterious cave 🕳️")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        forest_path(name)
    else:
        cave_path(name)

def forest_path(name):
    print(f"\n{name}, you enter the dark forest...")
    print("You see a river flowing nearby and a tall tree.")
    print("What will you do?")
    print("1. Follow the river 🌊")
    print("2. Climb the tree 🌳")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        river_path(name)
    else:
        print("\nYou climb the tree but slip and fall. Your adventure ends here. ❌")
        end_game(False)

def river_path(name):
    print(f"\n{name}, you follow the river and discover two things:")
    print("1. Try to swim across the river 🏊")
    print("2. Build a raft to cross the river 🛶")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        print("\nYou swim across but get swept away by the current. Game Over ❌")
        end_game(False)
    else:
        print("\nYou build a raft and safely cross the river, finding a chest full of treasure! 🏆🎉")
        end_game(True)

def cave_path(name):
    print(f"\n{name}, you enter the mysterious cave...")
    print("It’s very dark inside. You have two options:")
    print("1. Light a torch 🔥")
    print("2. Proceed in the dark 🌑")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        print("\nWith the torch, you see the treasure chest and claim it! 🏆🎉")
        end_game(True)
    else:
        print("\nYou stumble in the dark and fall into a pit. Game Over ❌")
        end_game(False)

def end_game(won):
    if won:
        print("\nCongratulations! You completed your quest successfully! 🥳")
    else:
        print("\nBetter luck next time, explorer.")

    if replay_prompt():
        start_game()
    else:
        print("\nThanks for playing! Goodbye 👋")

#Run the game
if __name__ == "__main__":
    start_game()