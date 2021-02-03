from Labs.Lab4.TransactionDetails import TransactionDetails


class TransactionData:
    transaction_history = []

    # def __int__(self):
    #     self.transaction_history = []

    def get_transaction_history(self):
        return self.transaction_history

    def print_transaction_history(self):
        order = 1
        for transaction in self.transaction_history:
            print("Transaction " + str(order) + ":")
            print(transaction)
            order += 1
            print("")

    def record_transaction(self, amount, budget_category, purchased_at, user):
        if self.check_budget(amount, budget_category, user):
            transaction_detail = TransactionDetails(amount, budget_category, purchased_at)
            self.make_transaction(amount, budget_category, user)
            self.transaction_history.append(transaction_detail)
            return transaction_detail

    def make_transaction(self, amount, budget_category, user):
        user_budgets = user.get_budgets()
        if budget_category in user_budgets:
            new_balance = user_budgets.get(budget_category) - amount
            user.set_budgets(budget_category, new_balance)
            user.set_balance(amount)

    def check_budget(self, amount, budget_category, user):
        user_budgets = user.get_budgets()
        if budget_category in user_budgets:
            if (user_budgets.get(budget_category) - amount) < 0:
                return False
            else:
                return True

    def show_budget_list(self):
        user_input = None
        while user_input != 5:
            print("\nSelect the budget category")
            print("-----------------------")
            print("1. Game and Entertainment")
            print("2. Clothing and Accessories")
            print("3. Eating Out")
            print("4. Miscellaneous")

            string_input = input("Please enter your choice (1 - 4) ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                return "Game and Entertainment"
            elif user_input == 2:
                return "Clothing and Accessories"
            elif user_input == 3:
                return "Eating Out"
            elif user_input == 4:
                return "Miscellaneous"
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")
