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

def zyra():
    while True:
        clear_screen()
        display_menu()
        choice = input(
            Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL
        )
        if choice == '1':
            clear_screen()
            print(
                Fore.CYAN +
                "\nYou selected Basic Information." +
                Style.RESET_ALL
            )
            print("Display basic information here.")
            input("\nPress Enter to continue...")
        elif choice == '2':
            clear_screen()
            print(
                Fore.CYAN +
                "\nYou selected Goals." +
                Style.RESET_ALL
            )
            print("Display goals here.")
            input("\nPress Enter to continue...")
        elif choice == '3':
            print(Fore.CYAN + "\nExiting..." + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED +
                "\nInvalid choice. Please try again." +
                Style.RESET_ALL
            )
            input("Press Enter to continue...")

zyra()
