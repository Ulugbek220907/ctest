#expense tracker program
expenses = {
    "Transportation": 0,
    "Food": 0,
    "Entertainment": 0
}

def print_expenses():
    print("==================\nExpense Categories:")
    for category in expenses:
        print("=>" + category + ": $" + str(expenses[category]))

print_expenses()
category = input("Enter the expense category(1-3, quit(4)): ")
expense = int(input("Enter the expense amount: "))

while category != "4":
    match category:
        case "1":
            expenses["Transportation"] += expense
        case "2":
            expenses["Food"] += expense
        case "3":
            expenses["Entertainment"] += expense
        case "4":
            print("Exiting the program...")
            break
        case _:
            print("Invalid category. Please enter a valid category.")
            category = input("Enter the expense category(1-3, quit(4)): ")
            continue
    print_expenses()
    category = input("Enter the expense category(1-3, quit(4)): ")
    expense = int(input("Enter the expense amount: "))
    