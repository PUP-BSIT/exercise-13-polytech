import os
import random
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
    print("3. Quote Maker")
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
            quote_maker()
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

def title_center(title, width=50):
    return Fore.MAGENTA + Style.BRIGHT + title.center(width) + Style.RESET_ALL

def display_basic_info():
    display_header()
    print(title_center("Basic Information"))
    print("-" * 50)
    print("Name: Annie Rose Raquem")
    print("Age: 20")
    print("Birthday: June 3, 2005")
    print("Birthplace: Taguig City")
    print("Course: BSIT")

def display_goals():
    display_header()
    print(title_center("Goals in Life"))
    print("-" * 50)
    print("1. Finish my degree.")
    print("2. Have a stable job.")
    print("3. Live a happy life.")
   

def quote_maker():
    display_header()
    print(title_center("Quote Maker"))
    print("-" * 50)
    quotes = [
        ("“The best way to predict the future is to create it.”",
         "Peter Drucker"),
        ("“Success is not final, failure is not fatal: It is the courage to "
         "continue that counts.”",
         "Winston Churchill"),
        ("“Believe you can and you’re halfway there.”",
         "Theodore Roosevelt"),
        ("“Your time is limited, so don’t waste it living someone else’s "
         "life.”",
         "Steve Jobs"),
        ("“Be yourself; everyone else is already taken.”",
         "Oscar Wilde")
    ]
    quote, author = random.choice(quotes)
    print("\n" + Fore.MAGENTA + f"{quote}")
    print(f"  — {author}\n")


def option_4():
    display_header()
    print(Fore.MAGENTA + "Option 4." + Style.RESET_ALL)

def option_5():
    display_header()
    print(Fore.MAGENTA + "Option 5." + Style.RESET_ALL)

def option_6():
    display_header()
    print(Fore.MAGENTA + "Option 6." + Style.RESET_ALL)

def option_7():
    display_header()
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
