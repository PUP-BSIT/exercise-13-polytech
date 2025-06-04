import time
import os

EXIT_OPTION = 0

def display_menu():
    print("_________________________________")
    print("  Victorio's information System  ")
    print("_________________________________")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Alarm Clock")
    print("4. Comment from Capilitan")
    print("5. Comment from Niones")
    print("6. Comment from Raquem")
    print("7. Comment from Villarta")
    print("0. Exit")
    print("________________________________")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def display_get_choice(choice):
    match choice:
        case 1:
            basic_information()
        case 2:
            goals()
        case 3:
            time_clock()
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case _:
            print("Invalid choice. Try again.")
    input("\nPress Enter to continue...")
 
def basic_information():
    print("Victorio's basic information: ")
    print("Full Name: Kalelle Mae Barcarse Victorio")
    print("Birthdate: December 11, 2004")
    print("Age: 20 years old")
    print("Hobbies: Playing video games, reading manhwa, and"
            " playing roblox")

def goals():
    print("Victorio's goals: ")
    print("- To graduate from college")
    print("- To have a cat")
    print("- To have a stable job")
    print("- To make my parents proud")

def time_clock():
    print("Time Clock")
    seconds = int(input("Enter countdown time in seconds: "))

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Overwrites the same line
        time.sleep(1)
        seconds -= 1

    print("Time's up! ⏰")

def kalelle():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == EXIT_OPTION:
            print("Exiting the system.")
            break

        os.system('cls')
        display_get_choice(choice)
        os.system('cls')

kalelle()





