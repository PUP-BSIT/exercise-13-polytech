import os
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
    print("3. for option 3")
    print("4. Comment teammate1")
    print("5. Comment teammate2")
    print("6. Comment teammate3")
    print("7. Comment teammate4")
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
            options()
        case 4:
            display_teammate_comment1()
        case 5:
            display_teammate_comment2()
        case 6:
            display_teammate_comment3()
        case 7:
            display_teammate_comment4()
        case 0:
            print(Fore.MAGENTA + "Thank you! Goodbye!\n")
            return
    input(Fore.GREEN + "\nPress Enter to continue...")

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
        "7. Live a life of purpose and peace."
    )

def options():
    display_header()
    print(Fore.CYAN + "Options." + Style.RESET_ALL)

def display_teammate_comment1():
    display_header()
    print(Fore.CYAN + "Option 4 comments." + Style.RESET_ALL)

def display_teammate_comment2():
    display_header()
    print(Fore.CYAN + "Option 5 comments." + Style.RESET_ALL)

def display_teammate_comment3():
    display_header()
    print(Fore.CYAN + "Option 6 comments." + Style.RESET_ALL)

def display_teammate_comment4():
    display_header()
    print(Fore.CYAN + "Option 7 comments." + Style.RESET_ALL)

def keith():
    while True:
        clear_screen()
        display_menu()
        choice = get_choice()
        if choice == EXIT_OPTION:
            process_choice(choice)
            break
        process_choice(choice)

keith()
