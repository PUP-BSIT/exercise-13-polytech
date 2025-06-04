import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50)
    print(" 🌸 Welcome to Annie Rose Raquem's Menu! 🌸")
    print("=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.MAGENTA + "Please choose an option:")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Exit" + Style.RESET_ALL)

def annie():
    while True:
        clear_screen()
        display_menu()
        choice = input(
            Fore.MAGENTA + "\nEnter your choice: " + Style.RESET_ALL
        )
        if choice == '1':
            print(
                Fore.MAGENTA +
                "You selected Basic Information." +
                Style.RESET_ALL
            )
            # Placeholder for processing code
            input("Press Enter to continue...")
        elif choice == '2':
            print(
                Fore.MAGENTA +
                "You selected Goals." +
                Style.RESET_ALL
            )
            # Placeholder for processing code
            input("Press Enter to continue...")
        elif choice == '3':
            print(Fore.MAGENTA + "Exiting..." + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED +
                "Invalid choice. Please try again." +
                Style.RESET_ALL
            )
            input("Press Enter to continue...")

annie()
