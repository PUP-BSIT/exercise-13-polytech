import os
import random
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50)
    print(" 🌸 Welcome to Annie Rose Raquem's Menu! 🌸")
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.CYAN + "Please choose an option:")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Quote Maker")
    print("4. Teammate Comment: zyra")
    print("5. Teammate Comment: Victorio")
    print("6. Teammate Comment: Person 3")
    print("7. Teammate Comment: Person 4")
    print("0. " + Fore.RED + "Exit" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + "-" * 50)

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
            display_teammate_comment("zyra")
        case 5:
            display_teammate_comment("victorio")
        case 6:
            display_teammate_comment("3")
        case 7:
            display_teammate_comment("4")
        case 0:
            exit_message()
        case _:
            invalid_choice_message()

def title_center(title, width=50):
    centered = title.center(width)
    return (Fore.LIGHTYELLOW_EX + Style.BRIGHT +
            centered[:80] + Style.RESET_ALL)

def display_basic_info():
    display_header()
    print(title_center("Basic Information"))
    print("-" * 50)
    print("Name: Annie Rose Raquem")
    print("Age: 20")
    print("Birthday: June 3, 2005")
    print("Birthplace: Taguig City")
    print("Course: BSIT")
    print("Year Level: 2nd Year")
    print("School: Polytechnic University of the Philippines")
    print("Hobbies: Reading, drawing, listening to music, coding")
    print("Favorite Color: Purple")
    print("Favorite Food: Avocado")

def display_goals():
    display_header()
    print(title_center("Goals in Life"))
    print("-" * 50)
    print("1. Finish my degree.")
    print("2. Have a stable job.")
    print("3. Live a happy life.")
    print("4. Travel to different countries.")
    print("5. Support my family.")
    print("6. Continuously learn and grow.")
    print("7. Make a positive impact on others.")
    print("8. Build my own tech startup.")
    print("9. Build my own personal business.")
    print("10. Write and publish a book.")
    print("11. Inspire young women in tech.")

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
    print(f"  — {author}")

def display_teammate_comment(teammate_name):
    display_header()
    print(title_center(f"Comment from {teammate_name}"))
    print("-" * 50)
    comments = {
        "1": "[Person 1 comment goes here]",
        "2": "[Person 2 comment goes here]",
        "3": "[Person 3 comment goes here]",
        "4": "[Person 4 comment goes here]",
    }
    print(comments.get(teammate_name, "[No comment available]"))

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
        input(Fore.GREEN + "\nPress Enter to continue...")

