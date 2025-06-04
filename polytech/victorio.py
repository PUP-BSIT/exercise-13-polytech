import time
import os

EXIT_OPTION = 0

def display_menu():
    #loop continues until the user enters 0
    print("_________________________________")
    print("  Victorio's information System  ")
    print("_________________________________")
    print(". Basic Information")
    print("2. Goals")
    print("3. Alarm Clock")
    print("4. Comment from Teammate 1")
    print("5. Comment from Teaammate 2")
    print("6. Comment from Teammate 3")
    print("7. Comment from Teammate 4")
    print("0. Exit")
    print("________________________________")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def process_choice(choice):
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            time_clock()
        case 4:
            display_teammate_comment()
        case 5:
            display_teammate_comment()
        case 6:
            display_teammate_comment()
        case 7:
            display_teammate_comment()
        case _:
            print("Invalid choice. Try again.")
    input("\nPress Enter to continue...")

def display_basic_info():
    print("Victorio's basic information: ")
    print("Full Name: Kalelle Mae Barcarse Victorio")
    print("Birthdate: December 11, 2004")
    print("Age: 20 years old")
    print("Hobbies: Playing video games, reading manhwa, and"
            " playing roblox")
    print("Favorite Color: Purple")

def display_goals():
    print("Victorio's goals: ")
    print("- To graduate from college")
    print("- To have a cat")
    print("- To have a stable job")
    print("- To make my parents proud")
    print("- To be happy and contented")
    print("- To be with someone I love")

def time_clock():
    print("Time Clock")
    seconds = int(input("Enter countdown time in seconds: "))

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Overwrites the same line
        time.sleep(1)
        seconds -= 1

    print("Time's up! ⏰")

def display_teammate_comment(teammate_name):
    print(f"Comment from {teammate_name}")
    comments = {
        "Teammate 1": "[Teammate 1's comment goes here]",
        "Teammate 2": "[Teammate 2's comment goes here]",
        "Teammate 3": "[Teammate 3's comment goes here]",
        "Teammate 4": "[Teammate 4's comment goes here]",
    }
    print(comments.get(teammate_name, "[No comment available]"))
    input("\nPress Enter to continue...")

def kalelle():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == EXIT_OPTION:
            print("Exiting the system.")
            break

        os.system('cls')
        process_choice(choice)
        os.system('cls')