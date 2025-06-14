import os
import random
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
    print("3. Odd or Even Game")
    print("4. Raquem Comment")
    print("5. niones_comment")
    print("6. Victorio Comment")
    print("7. Villarta Comment")
    print("0. Exit" + Style.RESET_ALL)

def display_basic_info():
    print("    💙🦋  Mikee's Basic Information  🦋💙")
    print("\nName: Mikee C. Capilitan.")
    print("Age: 20 years old.") 
    print("Sex: Female.")
    print("Birthday: December 5, 2004.")
    print("Civil Status: Single.")
    print("Religion: Roman Catholic.")
    print("School: Polytechnic University of the Philippines.")
    print("Course: Bachelor of Science in Information Technology (BSIT).")
    print("Favorite Color: Blue.")

def display_goals():
    print("    💙🦋  Mikee's Goals  🦋💙")
    print("\nHave a good life in the future.")
    print("Stay consistent and love oneself.")
    print("Have a decent job to help my family.")
    print("Own a business.")
    print("Travel to beautiful places around the world.")
    print("Continue learning and growing as a person.")

def odd_or_even():
    print("    💙🦋  Mikee's Even or Odd Game  🦋💙")
    print("\nI will give you a number. You tell me if it's even or odd.")
    print("Type 'exit' to quit.\n")

    while True:
        number = random.randint(1, 100)
        print(f"Number: {number}")
        answer = input("Is it even or odd? ").strip().lower()

        if answer == 'exit':
            print("Goodbye!")
            break

        if answer not in ['even', 'odd']:
            print("Please type 'even' or 'odd'.\n")
            continue

        correct = 'even' if number % 2 == 0 else 'odd'
        if answer == correct:
                print("Correct!\n")
        else:
                print(f"Wrong! It is {correct}.\n")

def raquem_comment():
    print(
        Fore.LIGHTBLUE_EX +
        "Nice work, Mikee! The layout is clean and the color scheme "
        "is very eye-catching! -Annie" +
        Style.RESET_ALL
    )

def niones_comment():
    print(
        Fore.LIGHTBLUE_EX +
        "Great use of emojis in headers, adds personality to the UI! - Zyra" +
        Style.RESET_ALL
    )

def victorio_comment():
    print(Fore.LIGHTBLUE_EX + "Good job, mikee!" + Style.RESET_ALL)

def villarta_comment():
    print(Fore.LIGHTBLUE_EX + "Nice - keith." + Style.RESET_ALL)

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            odd_or_even()
        case 4:
            raquem_comment()
        case 5:
            niones_comment()
        case 6:
            victorio_comment()
        case 7:
            villarta_comment()
        case 0:
            print(
                Fore.LIGHTBLUE_EX +
                "Have a Goodday, Goodbye!" +
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