import os
from colorama import Fore, Style, init

init(autoreset=True)

def display_header():
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "=" * 50)
    print("    💙🦋  Mikee Capilitan's Menu  🦋💙")
    print("=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.LIGHTBLUE_EX + "Please choose an option:")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Exit" + Style.RESET_ALL)

def mikee():
    while True:
        display_menu()
        choice = input(
            Fore.LIGHTBLUE_EX +
            "\nEnter your choice: " +
            Style.RESET_ALL
        )
        if choice == '1':
            print(
                Fore.LIGHTBLUE_EX +
                "You selected Basic Information." +
                Style.RESET_ALL
            )
            input("Press Enter to continue...")
        elif choice == '2':
            print(
                Fore.LIGHTBLUE_EX +
                "You selected Goals." +
                Style.RESET_ALL
            )
            input("Press Enter to continue...")
        elif choice == '3':
            print(
                Fore.LIGHTBLUE_EX +
                "Exiting..." +
                Style.RESET_ALL
            )
            break
        else:
            print(
                Fore.RED +
                "Invalid choice. Please try again." +
                Style.RESET_ALL
            )
            input("Press Enter to continue...")

mikee()