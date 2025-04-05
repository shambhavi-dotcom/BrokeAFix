NEEDS = ["Groceries", "Rent", "Utilities", "Transport"]
WANTS = ["Food Delivery", "Entertainment", "Shopping", "Subscriptions"]

def classify_expense(category):
    if category in NEEDS:
        return "Need"
    elif category in WANTS:
        return "Want"
    else:
        return "Uncategorized"
