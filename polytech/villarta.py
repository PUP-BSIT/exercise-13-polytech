import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_header():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print("🌟 Welcome to keith's Info Menu! 🌟")
    print("=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.CYAN + "\nMenu:")
    print(Fore.YELLOW + "1. Basic Information")
    print("2. Goals")
    print("3. for option 3")
    print("4. Comment teammate1")
    print("5. Comment teammate2")
    print("6. Comment teammate3")
    print("7. Comment teammate4")
    print(Fore.RED + "0. Exit")

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            options()
        case 4:
            display_teammate_comment1()
        case 5:
            display_teammate_comment2()
        case 6:
            display_teammate_comment3()
        case 7:
            display_teammate_comment4()
        case 0:
            print(Fore.MAGENTA + "Thank you! Goodbye!\n")

def display_basic_info():
    print(Fore.CYAN + "My Basic Information is here." + Style.RESET_ALL)

def display_goals():
    print(Fore.CYAN + "Goals is here." + Style.RESET_ALL)

def options():
    print(Fore.CYAN + "Options." + Style.RESET_ALL)

def display_teammate_comment1():
    print(Fore.CYAN + "Option 4 comments." + Style.RESET_ALL)

def display_teammate_comment2():
    print(Fore.CYAN + "Option 5 comments." + Style.RESET_ALL)

def display_teammate_comment3():
    print(Fore.CYAN + "Option 6 comments." + Style.RESET_ALL)

def display_teammate_comment4():
    print(Fore.CYAN + "Option 7 comments." + Style.RESET_ALL)

def keith():
    while True:
        clear_screen()
        display_menu()
        try:
            choice = int(
                input(
                    Fore.CYAN +
                    "\nEnter your choice: " +
                    Style.RESET_ALL
                )
            )
        except ValueError:
            choice = -1
        process_choice(choice)
        if choice == 0:
            break
        input("Press Enter to continue...")

keith()