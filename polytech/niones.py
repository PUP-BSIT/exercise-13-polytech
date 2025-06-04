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
    print("3. View Minecraft Character")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("7. Option 7")
    print("0. Exit" + Style.RESET_ALL)

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            option_3()
        case 4:
            option_4()
        case 5:
            option_5()
        case 6:
            option_6()
        case 7:
            option_7()
        case 0:
            print(
                Fore.CYAN +
                "Thank you and Goodbye!" +
                Style.RESET_ALL
            )
        case _:
            print(
                Fore.CYAN +
                "Invalid choice. Please try again." +
                Style.RESET_ALL
            )

def display_basic_info():
    print(Fore.CYAN + "Basic Information goes here." + Style.RESET_ALL)
  

def display_goals():
    print(Fore.CYAN + "Goals go here." + Style.RESET_ALL)


def option_3():
    print(Fore.CYAN + "Option 3." + Style.RESET_ALL)


def option_4():
    print(Fore.CYAN + "Option 4." + Style.RESET_ALL)


def option_5():
    print(Fore.CYAN + "Option 5." + Style.RESET_ALL)


def option_6():
    print(Fore.CYAN + "Option 6." + Style.RESET_ALL)


def option_7():
    print(Fore.CYAN + "Option 7." + Style.RESET_ALL)

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
