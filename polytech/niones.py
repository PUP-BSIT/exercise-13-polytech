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
    display_header()
    print(Fore.CYAN + "Basic Information goes here." + Style.RESET_ALL)
    print("-" * 50)
    print(
        "Hello! I'm Zyra Joy O. Niones, a 20-year-old student currently\n"
        "taking up a Bachelor of Science in Information Technology at the\n"
        "Polytechnic University of the Philippines. Among the different\n"
        "areas in IT, I’ve grown to enjoy frontend development the most, as\n"
        "it beautifully blends technology with creativity. Although I'm not\n"
        "yet a fully skilled frontend developer, I am eager to learn more\n"
        "and hone my skills in this area. This interest closely connects to\n"
        "my long-time passion for art—especially traditional forms like\n"
        "sculpture and drawing. Through frontend work, I get to express that\n"
        "same artistic energy in designing user-friendly and visually\n"
        "appealing interfaces."
    )
    input("\nPress Enter to continue...")
  

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
        try:
            choice = int(
                input(
                    Fore.CYAN +
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
zyra()


