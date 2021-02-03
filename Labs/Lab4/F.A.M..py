from Labs.Lab4.User import User
from Labs.Lab4.TransactionData import TransactionData


class FamilyAppointedModerator:
    def __init__(self, user, transaction_data):
        self.user = user
        self.transaction_data = transaction_data

    def show_menu(self):
        user_input = None
        while user_input != 5:
            print("\nWelcome to the F.A.M. menu!")
            print("-----------------------")
            print("1. Record Transaction")
            print("2. Check the balance")
            print("3. View Transaction History")
            print("4. View Budgets")
            print("5. Quit")
            string_input = input("Please enter your choice (1-5) ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.record_transaction_menu()
            elif user_input == 2:
                print("\nCurrent balance is $" + str(self.user.get_balance()))
            elif user_input == 3:
                print("\nTransaction History:")
                self.transaction_data.print_transaction_history()
            elif user_input == 4:
                print("\nHere is the budgets")
                print(self.user.get_budgets())
            elif user_input == 5:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

        print("\nThanks for using our service!")

    def record_transaction_menu(self):
        print("\nWelcome to Transaction Menu!")
        amount = float(input("Type the amount: "))
        budget_category = self.transaction_data.show_budget_list()
        purchased_at = input("Purchased at: ")
        transaction = self.transaction_data.record_transaction(amount, budget_category, purchased_at, self.user)
        if transaction:
            print("\nTransaction was successful.")
            print("Here is the detail of your transaction.")
            print(transaction)
        else:
            print("Transaction failed.")


def load_test_user():
    username = "Timmy"
    balance = 80.00
    budgets = {
        "Game and Entertainment": 20.00,
        "Clothing and Accessories": 20.00,
        "Eating Out": 20.00,
        "Miscellaneous": 20.00
    }
    user = User(username, balance, budgets)
    return user


def main():
    user = load_test_user()
    transaction_data = TransactionData()
    fam = FamilyAppointedModerator(user, transaction_data)
    fam.show_menu()


if __name__ == '__main__':
    main()
