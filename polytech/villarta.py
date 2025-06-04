import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

EXIT_OPTION = 0

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_header():
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50)
    print("🌟 Welcome to My Personal Info Menu! 🌟")
    print("=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.CYAN + "\nMenu:")
    print(Fore.YELLOW + "1. Basic Information")
    print("2. Goals")
    print("3. creative")
    print("4. Comment teammate1")
    print("5. Comment teammate2")
    print("6. Comment teammate3")
    print("7. Comment teammate4")
    print(Fore.RED + "0. Exit")

def get_choice():
    while True:
        try:
            choice = int(input(Fore.CYAN + "\nEnter your choice: "))
            if choice in range(0, 8 + 1):
                return choice
            else:
                print(Fore.RED + "Invalid choice. Try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

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
            print(Fore.MAGENTA + "\nThank you! Goodbye!\n")

def display_basic_info():
    print(Fore.MAGENTA + "My Basic Information is here." + Style.RESET_ALL)

def display_goals():
    print(Fore.MAGENTA + "Goals is here." + Style.RESET_ALL)

def options():
    print(Fore.MAGENTA + "Option 3." + Style.RESET_ALL)

def display_teammate_comment1():
    print(Fore.CYAN + "Option 4." + Style.RESET_ALL)

def display_teammate_comment2():
    print(Fore.CYAN + "Option 5." + Style.RESET_ALL)

def display_teammate_comment3():
    print(Fore.CYAN + "Option 6." + Style.RESET_ALL)

def display_teammate_comment4():
    print(Fore.CYAN + "Option 7." + Style.RESET_ALL)

def keith():
    while True:
        clear_screen()
        display_menu()
        choice = get_choice()
        if choice == EXIT_OPTION:
            process_choice(choice)
            break
        process_choice(choice)

keith()