def add_expense(expenses, total, amount):
    expenses.append(amount)
    total += amount
    return total


def show_report(expenses, total):
    print("\n" + "="*30)
    print("      EXPENSE REPORT")
    print("="*30)
    for i, exp in enumerate(expenses, start=1):
        print(f"  {i}. ₹{exp:.2f}")
    print("-"*30)
    print(f"  Transactions : {len(expenses)}")
    print(f"  Total Spent  : ₹{total:.2f}")
    print("="*30)


def main():
    print("===== DecodeLabs Expense Tracker =====")
    print("Type an amount to add. Type 'done' to finish.\n")

    expenses = []
    total = 0.0

    while True:
        user_input = input("Enter expense (or 'done'): ").strip()

        if user_input.lower() == 'done':
            break

        try:
            expense = float(user_input)
            if expense < 0:
                print("Amount can't be negative. Try again.")
                continue
            total = add_expense(expenses, total, expense)
            print(f"  Added ₹{expense:.2f} | Running total: ₹{total:.2f}")
        except ValueError:
            print("  Invalid input. Enter a number like 100 or 49.99")

    if expenses:
        show_report(expenses, total)
    else:
        print("No expenses entered.")


if __name__ == "__main__":
    main()