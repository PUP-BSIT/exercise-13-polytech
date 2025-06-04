import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print("    💙🦋  Mikee Capilitan's Menu  🦋💙")
    
def display_menu():
    display_header()
    print(Fore.LIGHTBLUE_EX + "\nPlease choose an option:")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("7. Option 7")
    print("0. Exit" + Style.RESET_ALL)

def display_basic_info():
    print("    💙🦋  Mikee's Basic Information  🦋💙")

    print("\nName: Mikee . Capilitan. ")
    print("Age: 20 years old. ") 
    print("Sex: Female. ")
    print("Birthday: December 5, 2004. ")
    print("Civil Status: Single. ")
    print("Religion: Roman Catholic. ")
    print("Course: Bachelor of Science in Information Technology (BSIT). ")

def display_goals():
    print(Fore.LIGHTBLUE_EX + "Goals go here." + Style.RESET_ALL)

def option_3():
    print(Fore.LIGHTBLUE_EX + "Option 3." + Style.RESET_ALL)

def option_4():
    print(Fore.LIGHTBLUE_EX + "Option 4." + Style.RESET_ALL)

def option_5():
    print(Fore.LIGHTBLUE_EX + "Option 5." + Style.RESET_ALL)

def option_6():
    print(Fore.LIGHTBLUE_EX + "Option 6." + Style.RESET_ALL)

def option_7():
    print(Fore.LIGHTBLUE_EX + "Option 7." + Style.RESET_ALL)

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
                Fore.LIGHTBLUE_EX +
                "Thank you for using this menu! Goodbye!" +
                Style.RESET_ALL
            )
        case _:
            print(
                Fore.RED +
                "Invalid choice. Please try again." +
                Style.RESET_ALL
            )

def mikee():
    while True:
        clear_screen()
        display_menu()
        try:
            choice = int(
                input(
                    Fore.LIGHTBLUE_EX +
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

mikee()