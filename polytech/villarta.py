import os
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

EXIT_OPTION = 0

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_header():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print("🌟 Welcome to Keith's Info Menu! 🌟")
    print("=" * 50 + Style.RESET_ALL)

def display_menu():
    display_header()
    print(Fore.CYAN + "\nMenu:")
    print(Fore.YELLOW + "1. Basic Information")
    print("2. Goals")
    print("3. Random Fun Facts")
    print("4. Raquem comment")
    print("5. Niones comment")
    print("6. Victorio comment")
    print("7. Capilitan comment")
    print(Fore.RED + "0. Exit")

def get_choice():
    while True:
        try:
            choice = int(input(Fore.CYAN + "\nEnter your choice: "))
            if choice in range(0, 8 + 1):
                return choice
            else:
                print(Fore.RED + "Invalid choice. Try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            fun_fact_maker()
        case 4:
            raquem_comment()
        case 5:
            niones_comment()
        case 6:
            display_teammate_comment3()
        case 7:
            capilitan_comment()
        case 0:
            print(Fore.MAGENTA + "Thank you! Goodbye!\n")
            return

def display_basic_info():
    display_header()
    print(Fore.CYAN + "Basic Information")
    print("-" * 40)
    print(
        "I am a 20-year-old college student currently taking up\n"
        "Information Technology. I enjoy watching series and\n"
        "movies during my free time, and I love playing mobile\n"
        "games whenever I have extra time to relax and unwind.\n"
        "\n"
        "I am also passionate about learning how to dance and\n"
        "express myself through movement. In addition, I enjoy\n"
        "taking random photos of simple yet beautiful moments\n"
        "like the moon, sunsets, sunrises, or even rainy days\n"
        "as a way to appreciate life and its everyday beauty."
    )

def display_goals():
    display_header()
    print(Fore.CYAN + "Goals in Life")
    print("-" * 40)
    print(
        "1. Achieve financial stability.\n"
        "2. Experience happiness with family.\n"
        "3. Build strong relationships.\n"
        "4. Grow emotionally and intellectually.\n"
        "5. Finish studies and pursue a career or business.\n"
        "6. Help those in need.\n"
        "7. Live a life of purpose and peace.\n"
        "8. Travel and explore new cultures.\n"
        "9. Continuously learn new skills.\n"
        "10. Inspire others to reach their potential."
    )

def options():
    display_header()
    print(Fore.CYAN + "Options." + Style.RESET_ALL)

def raquem_comment():
    display_header()
    print(
        Fore.CYAN +
        "The fun facts feature is super creative—really makes the "
        "program fun! -Annie" +
        Style.RESET_ALL
    )

def niones_comment():
    display_header()
    print(
        Fore.CYAN +
        "The layout and color choices make everything easy to "
        "follow. -zyra" +
        Style.RESET_ALL
    )

def display_teammate_comment3():
    display_header()
    print(Fore.CYAN + "Option 6 comments." + Style.RESET_ALL)

def capilitan_comment():
    display_header()
    print(Fore.CYAN + "Option 7 comments." + Style.RESET_ALL)

def fun_fact_maker():
    display_header()
    print(Fore.CYAN + "Random Fun Fact")
    print("-" * 40)

    facts = [
        "Honey never spoils.",
        "Bananas are actually berries!",
        "Octopuses have three hearts.",
        "Strawberries aren't real berries.",
        "The Eiffel Tower grows taller in summer.",
        "You blink around 20 times a minute.",
        "Some cats are allergic to humans.",
        "There are more stars than grains of sand.",
        "A group of flamingos is called a flamboyance.",
        "The moon has moonquakes caused by gravity."
    ]

    fact = random.choice(facts)
    print(Fore.YELLOW + fact)

def keith():
    while True:
        clear_screen()
        display_menu()
        choice = get_choice()
        if choice == EXIT_OPTION:
            process_choice(choice)
            break
        process_choice(choice)
        input(Fore.GREEN + "\nPress Enter to continue...")