UNSET_OPTION = 0
EXIT_OPTION = 8

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
    print("8. Exit")
    print("________________________________")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return UNSET_OPTION

def display_get_choice(choice):
    match choice:
        case 1:
            basic_information()
        case 2:
            pass
        case 3:
            pass
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

def basic_information():
    print("Victorio's basic information: ")
    print("Full Name: Kalelle Mae Barcarse Victorio")
    print("Birthdate: December 11, 2004")
    print("Age: 20 years old")
    print("Hobbies: Playing video games, reading manhwa, and"
            " playing roblox")

def kalelle():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == EXIT_OPTION:
            print("Exiting the system.")
            break

        display_get_choice(choice)

kalelle()





