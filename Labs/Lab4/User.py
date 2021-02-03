class User:
    def __init__(self, username, balance, budgets):
        self.username = username
        self.balance = balance
        self.budgets = budgets

    def get_balance(self):
        return self.balance

    def get_budgets(self):
        return self.budgets

    def set_balance(self, amount):
        self.balance = self.balance - amount

    def set_budgets(self, budget_category, amount):
        self.budgets[budget_category] = amount
