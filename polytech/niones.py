import os 
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(" 🐱 Welcome to Zyra Joy O. Niones' Menu! 🐱")
    print("=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.CYAN + "Please choose an option:")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Exit" + Style.RESET_ALL)

def process_choice(choice):
    clear_screen()
    match choice:
        case '1':
            print(Fore.CYAN + "\nYou selected Basic Information." + Style.RESET_ALL)
            print("Display basic information here.")
        case '2':
            print(Fore.CYAN + "\nYou selected Goals." + Style.RESET_ALL)
            print("Display goals here.")
        case '3':
            print(Fore.CYAN + "\nExiting..." + Style.RESET_ALL)
        case _:
            print(Fore.RED + "\nInvalid choice. Please try again." + Style.RESET_ALL)

def zyra():
    while True:
        clear_screen()
        display_menu()
        choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)
        process_choice(choice)
        if choice == '3':
            break
        input(Fore.CYAN + "\nPress Enter to continue..." + Style.RESET_ALL)

zyra()
