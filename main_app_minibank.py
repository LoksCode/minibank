import time


# --------------------------------------------- funkcje ---------------------------------------------

client_list = ["client1", "client2", "client3"]
password_list = ["pw123", "pw456", "pw789"]


def cash_deposit(a, balance):
    return balance + a


def cash_withdraw(a, balance):
    return balance - a


def main_loop():
    while True:
        balance = 0
        command = input("What do you want to do?\n> ")
        if command.lower() == "help":
            print("Available commands: \n>DEPOSIT \n>WITHDRAW \n>BALANCE \n>EXIT\n")
        elif command.lower() == "deposit":
            try:
                a = float(input("insert deposit amount: "))
                balance = cash_deposit(a, balance)
                print(f"{a}PLN has been deposited. Balance: {balance}.")
            except ValueError:
                print("Deposit amount must be an number.")
        elif command.lower() == "wyithdraw":
            if balance > 0:
                try:
                    a = float(input("kwota wypłaty: "))
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
        elif command.lower() == "exit":
            print("End of program.")
            print("Goodbye!")
            break
        else:
            print("Unknown command. Type HELP for available commands..")


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


print("Welcome to minibank! \n\nPlease log in:\n")
print("--Login--\n")
log_in_procedure()
print("Welcome to minibank! \n\ntype HELP to view commands...")
main_loop()

