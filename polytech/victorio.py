import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

EXIT_OPTION = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print(Fore.MAGENTA + "_________________________________")
    print(Fore.MAGENTA + "  Victorio's Information System  ")
    print(Fore.MAGENTA + "_________________________________")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Alarm Clock")
    print("4. Raquem comment")
    print("5. Comment from Teammate 2")
    print("6. Comment from Teammate 3")
    print("7. Comment from Teammate 4")
    print("0. Exit")
    print(Fore.MAGENTA + "________________________________")

def get_user_choice():
    try:
        return int(input(Fore.MAGENTA + "Enter choice: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        return None

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            timer_clock()
        case 4:
            display_teammate_comment("Raquem")
        case 5:
            display_teammate_comment("Teammate 2")
        case 6:
            display_teammate_comment("Teammate 3")
        case 7:
            display_teammate_comment("Teammate 4")
        case _:
            print(Fore.RED + "Invalid choice. Try again.")
    input(Fore.CYAN + "\nPress Enter to continue...")

def display_basic_info():
    print(Fore.BLUE + "Victorio's Basic Information:")
    print(Fore.MAGENTA + "- Full Name     : Kalelle Mae Barcarse Victorio")
    print("- Birthdate     : December 11, 2004")
    print("- Age           : 20 years old")
    print("- Hobbies       : Playing video games, reading manhwa, playing Roblox")
    print("- Favorite Color: Purple")

def display_goals():
    print(Fore.BLUE + "Victorio's Goals:")
    goals = [
        "- To graduate from college",
        "- To have a cat",
        "- To have a stable job",
        "- To make my parents proud",
        "- To be happy and contented",
        "- To be with someone I love"
    ]
    for goal in goals:
        print(Fore.MAGENTA + goal)

def timer_clock():
    print(Fore.BLUE + "Time Clock")
    try:
        seconds = int(input(Fore.MAGENTA + "Enter countdown time in seconds: "))
        if seconds <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Please enter a valid positive integer.")
        return

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(Fore.MAGENTA + timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print(Fore.CYAN + "Time's up! ⏰")

def display_teammate_comment(teammate_name):
    print(Fore.BLUE + f"Comment from {teammate_name}")
    comments = {
        "Raquem": "Clean structure and very readable—great job, Kalelle!",
        "Teammate 2": "[Teammate 2's comment goes here]",
        "Teammate 3": "[Teammate 3's comment goes here]",
        "Teammate 4": "[Teammate 4's comment goes here]",
    }
    print(Fore.MAGENTA + comments.get(teammate_name, "[No comment available]"))

def kalelle():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_choice()
        if choice is None:
            input(Fore.CYAN + "Press Enter to continue...")
            continue

        if choice == EXIT_OPTION:
            print(Fore.CYAN + "Exiting the system.")
            break

        process_choice(choice)
