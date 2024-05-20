class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item['description'][:23]
            amount = '{:.2f}'.format(item['amount'])
            total += item['amount']
            items += f"{description:<23}{amount:>7}\n"
        output = title + items + f"Total: {total}"
        return output


def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent -= item['amount']
        spent.append(round(total_spent, 2))
        category_names.append(category.name)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent) * 100, 2))

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    -" + "---" * len(category_names) + "\n"
    longest_name_length = max([len(name) for name in category_names])

    for i in range(longest_name_length):
        graph += "     "
        for name in category_names:
            if i >= len(name):
                graph += "   "
            else:
                graph += name[i] + "  "
        if i < longest_name_length - 1:
            graph += "\n"

    return graph
food = Category("Tin")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Tung")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
