import time

def introduction():
    print("Welcome to Monkey Island Adventure!")
    print("You are on a quest to find the legendary treasure of Monkey Island.")

def choose_path():
    print("You find two paths:")
    print("1. Take the dangerous jungle path.")
    print("2. Sail through waters infested with pirates.")
    choice = input("Enter 1 or 2: ")
    return choice

def jungle_route():
    print("You enter a thick jungle with strange creatures.")
    time.sleep(1)
    print("An old man appears and offers to guide you.")
    time.sleep(1)
    print("Do you trust him?")
    print("1. Trust the old man.")
    print("2. Decline and go on your own.")
    choice = input("Enter 1 or 2: ")
    return choice

def pirate_waters():
    print("You set sail through dangerous waters with pirates.")
    time.sleep(1)
    print("Pirates approach, demanding your treasure map.")
    time.sleep(1)
    print("What will you do?")
    print("1. Give them the map.")
    print("2. Try to escape from the pirates.")
    choice = input("Enter 1 or 2: ")
    return choice

def end_game(outcome):
    if outcome == "win":
        print("Congratulations! You found the legendary treasure of Monkey Island!")
    else:
        print("Game over. Better luck next time!")

def main():
    introduction()
    path_choice = choose_path()
    if path_choice == "1":
        jungle_choice = jungle_route()
        if jungle_choice == "1":
            print("The old man leads you safely to the treasure.")
            end_game("win")
        else:
            print("You get lost in the jungle and never find the treasure.")
            end_game("lose")
    elif path_choice == "2":
        pirate_choice = pirate_waters()
        if pirate_choice == "1":
            print("The pirates take your map and leave. You continue your journey.")
            time.sleep(1)
            print("After some challenges, you discover the treasure!")
            end_game("win")
        else:
            print("You try to escape from the pirates, but they catch you.")
            end_game("lose")
    else:
        print("Invalid choice. Game over.")
if __name__ == "__main__":
    main()
