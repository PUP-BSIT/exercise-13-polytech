import os

import tkinter as tk
from io import BytesIO

import requests
from PIL import Image, ImageTk

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
    print("4. Raquem comment")
    print("5. Victorio comment")
    print("6. Capilitan comment")
    print("7. villarta comment")
    print("0. Exit" + Style.RESET_ALL)

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            display_minecraft_character()
        case 4:
            Raquem_comment()
        case 5:
            option_5()
        case 6:
            capilitan_comment()
        case 7:
            villarta_comment()
        case 0:
            print(
                Fore.CYAN +
                "Thank you and Have a Good day. Padayon!" +
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

def display_goals():
    display_header()
    print(Fore.CYAN + "Goals go here." + Style.RESET_ALL)
    print("-" * 50)
    print("1. To survive and thrive in college life.")
    print("2. To graduate as a skilled and knowledgeable person.")
    print("3. To become a skilled UX/UI designer.")
    print("4. To stay motivated in all aspects of life.")
    print("5. To be more faithful to God.")
    print("6. To maintain a healthy lifestyle "
          "and regulate my menstrual cycle.")
    print("7. To survive summer class.")
    print("8. To be a servant of God.")
    print("9. To Donate my hair once i reached the expected length.")

def display_minecraft_character():
    display_header()
    print(Fore.CYAN + "Minecraft Character Viewer." + Style.RESET_ALL)
    print(Fore.CYAN + "Please wait..." + Style.RESET_ALL)
    print("-" * 50)
    url = (
        "https://crafatar.com/avatars/"
        "c2e45a26-3395-47ff-86c0-b3dd0c2aa2d2"
        "?scale=10&overlay=true"
    )

    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

        root = tk.Tk()
        root.title("Zyra's Minecraft Character")

        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()

        root.mainloop()

    except Exception as e:
        print("Error loading Minecraft avatar:", e)
        input("\nPress Enter to continue...")

def Raquem_comment():
    print(
        Fore.CYAN +
        "Awesome touch with the Minecraft character viewer — "
        "it's so unique! -Annie" +
        Style.RESET_ALL
    )

def option_5():
    print(Fore.CYAN + "Option 5." + Style.RESET_ALL)

def capilitan_comment():
    print(Fore.CYAN + "Nice use of colorama for a clean! -mikee" + 
        Style.RESET_ALL)

def villarta_comment():
    print(Fore.CYAN + "Nice Code! - keith." + Style.RESET_ALL)

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