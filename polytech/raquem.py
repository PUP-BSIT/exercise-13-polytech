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
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("7. Option 7")
    print("0. Exit" + Style.RESET_ALL)

def display_basic_info():
    print(Fore.MAGENTA + "Basic Information goes here." + Style.RESET_ALL)
    
def display_goals():
    print(Fore.MAGENTA + "Goals go here." + Style.RESET_ALL)

def option_3():
    print(Fore.MAGENTA + "Option 3." + Style.RESET_ALL)

def option_4():
    print(Fore.MAGENTA + "Option 4." + Style.RESET_ALL)

def option_5():
    print(Fore.MAGENTA + "Option 5." + Style.RESET_ALL)

def option_6():
    print(Fore.MAGENTA + "Option 6." + Style.RESET_ALL)

def option_7():
    print(Fore.MAGENTA + "Option 7." + Style.RESET_ALL)

def exit_message():
    print(
        Fore.CYAN + Style.BRIGHT +
        "=======================================\n" +
        "🌸 Thank you for visiting! Goodbye! 🌸\n" +
        "=======================================" +
        Style.RESET_ALL
    )

def invalid_choice_message():
    print(
        Fore.RED + Style.BRIGHT +
        "========================================\n" +
        "❌ Invalid choice. Please try again. ❌\n" +
        "========================================" +
        Style.RESET_ALL
    )

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
            exit_message()
        case _:
            invalid_choice_message()

def annie():
    while True:
        clear_screen()
        display_menu()
        try:
            choice = int(
                input(
                    Fore.MAGENTA +
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

annie()
