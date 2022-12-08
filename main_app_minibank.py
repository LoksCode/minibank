import time
import random


# --------------------------------------------- funkcje ---------------------------------------------

client_list = ["client1", "client2", "client3"]
password_list = ["pw123", "pw456", "pw789"]

def cards_options():
    print('1. Add new card.')
    print('2. Restrict a card.')
    print('3. Show list of your cards.')
    print('4. Exit')

def commands_available():
    print("\nAvailable commands: \n>DEPOSIT \n>WITHDRAW \n>BALANCE \n>CARDS \n>EXIT")


def cash_deposit(a, balance):
    return balance + a


def cash_withdraw(a, balance):
    return balance - a


def pick_option():
    while True:
        i = input('\nWhat do you want to do? (1-4): ')
        try:
            numb = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= numb <= 4:
            return numb
        print('This must be a number between 1 and 4.')


def cards_add():
    card = random.randint(1000, 9999)
    cards_active.append(card)
    return card


def cards_restrict():
    task = int(input("Insert 4-digit number of a card that is going to be restricted: "))
    if task >= 1000 and task <= 9999:
        cards_active.remove(task)
        cards_restricted.append(task)
    else:
        print("\nERROR: This must be an 4-digit number. Please try again.")
    return task


def cards_main_loop():
    while True:
        cards_options()
        option = pick_option()
        if option == 1:
            print("\nCard no.", cards_add(), "was added to your account.")
        elif option == 2:
            print("\nActive cards:")
            for numer, crd_numb in enumerate(cards_active):
                print(numer + 1, crd_numb)
            print("\nCard no.", cards_restrict(), "has been restricted.")
        elif option == 3:
            print("Active cards:")
            for numer, crd_numb in enumerate(cards_active):
                print(numer + 1, crd_numb)
            print("Restricted cards:")
            for numer, crd_numb in enumerate(cards_restricted):
                print(numer + 1, crd_numb)
        elif option == 4:
            return


def main_loop():
    balance = 0
    while True:
        (commands_available())
        command = input("\nWhat do you want to do?\n> ")
        if command.lower() == "help":
            (commands_available())
        elif command.lower() == "deposit":
            try:
                a = float(input("insert deposit amount: "))
                balance = cash_deposit(a, balance)
                print(f"{a}PLN has been deposited. Balance: {balance}.")
            except ValueError:
                print("Deposit amount must be an number.")
        elif command.lower() == "withdraw":
            if balance > 0:
                try:
                    a = float(input("insert withdraw amount: "))
                    if a <= balance:
                        balance = cash_withdraw(a, balance)
                        print(f"{a}PLN has been withdrawn. Balance: {balance}.")
                    else:
                        print(f"Insufficient funds. Your balance is:{balance}.")
                except ValueError:
                    print("Withdraw amount must be an number.")
            else:
                print(f"Insufficient funds. Your balance is:{balance}.")
        elif command.lower() == "balance":
            print(f"Your balance is: {balance}PLN")
        elif command.lower() == "cards":
            cards_main_loop()
        elif command.lower() == "exit":
            print("End of program.")
            print("Goodbye!")
            break
        else:
            print("Unknown command. Type HELP for available commands...")


def log_in_procedure():
    pw_tries = 0
    while pw_tries <= 2:
        username = input("Please enter your username: ")
        if username in client_list:
            password = input("Please enter your password: ")
            if password in password_list:
                print("Successfully logged in!!\n")
                break
            else:
                pw_tries += 1
                print("Incorrect password")
        else:
            print("User not found - try again.")
    else:
        print("Too many attempts - account has been blocked...")
        quit()


cards_active = []
cards_restricted = []

print("Welcome to minibank! \n\nPlease log in:\n")
print("--Login--\n")
log_in_procedure()
print("Welcome to minibank! \n\ntype HELP to view commands...")
main_loop()

