from random import randint

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Customer(Person):
    account_number = randint(359019, 402190)

    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name)
        self.balance = balance

    def __str__(self):
        return f"Your available balance is {self.balance}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Your have deposited {deposit_amount}. Your new balance is £{self.balance}")

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f"You have withdrawn £{withdraw_amount}. Your balance is now £{self.balance}")
        else:
            print("Your remaining balance is not enough to perform this operation")


def create_client():
    first_name = input("Please, enter your first name\n").capitalize()
    last_name = input("Please, enter your last name\n").capitalize()
    balance = int(input("Please, input the number amount you would like to deposit at this time\n"))

    new_customer = Customer(first_name, last_name, balance)
    print(f"""Hello, {first_name} {last_name}. Welcome to Online Banking.\n
    Your account number is {new_customer.account_number}\n""")
    return new_customer

def main():
    new_customer = create_client()

    choice = input("""What would you like to do at this time?\n
    a - View your balance
    b - Withdraw funds
    c - Deposit funds
    d - Exit\n""").lower()

    while True:

        if choice == "a":
                print(new_customer)

        elif choice == "b":
            try:
                withdraw_amount = int(input("Please, input the amount you would like to withdraw\n"))
                return new_customer.withdraw(withdraw_amount)
            except ValueError:
                    print("Please, make sure to input the correct amount")

        elif choice =="c":
            try:
                deposit_amount = int(input("Please, input the amount you would like to deposit\n"))
                return new_customer.deposit(deposit_amount)
            except ValueError:
                    print("Please, make sure to input the correct amount\n")
            return new_customer.deposit()

        elif choice == "d":
            break

    else:
        print("Please make sure you choose one of the options above ")

main()

