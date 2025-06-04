from polytech import niones, raquem
from polytech import capilitan
import os

UNSET_OPTION = 0
EXIT_OPTION = 6

def clear_screen():
    os.system('cls')

def display_menu():
    print("================================")
    print("              Menu              ")
    print("================================")
    print("1. ")
    print("2. Zyra Joy O. Niones Module")
    print("3. Annie Rose S. Raquem Module")
    print("1. Mikee C. Capilitan Module")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Exit")
    print("================================")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return UNSET_OPTION

def display_get_choice(choice):
    match choice:
        case 1:
            capilitan.mikee()
        case 2:
            niones.zyra()
            pass
        case 3:
            raquem.annie()
        case 4:
            #TO-DO(Villarta): call your module here
            pass
        case 5:
            #TO-DO(Victorio): call your module here
            pass
        case _:
            print("Invalid choice. Try again.")
    input("Press Enter to continue...")

def main():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_choice()


        if choice == EXIT_OPTION:
            print("Exiting the system.")
            break

        display_get_choice(choice)

main()





