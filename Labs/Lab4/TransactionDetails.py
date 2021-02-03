import datetime


class TransactionDetails:
    def __init__(self, amount, budget_category, purchased_at):
        self.time = str(datetime.datetime.now())[:19]
        self.amount = amount
        self.budget_category = budget_category
        self.purchased_at = purchased_at

    def get_time(self):
        return self.time

    def get_amount(self):
        return self.amount

    def get_budget_category(self):
        return self.budget_category

    def get_purchased_at(self):
        return self.purchased_at

    def __str__(self):
        return f"Time: {self.get_time()}\n" \
               f"Amount: {self.get_amount()}\n" \
               f"Budget Category: {self.get_budget_category()}\n" \
               f"Purchased at: {self.get_purchased_at()}"
