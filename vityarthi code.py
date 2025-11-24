def financial_keeper():
    """
    A simple financial transaction keeper to calculate monthly savings.
    It takes user input for salary, expenses, and taxes paid.
    """
    print("--- Monthly Financial Transaction Keeper ---")

    # 1. Get Monthly Income (Salary)
    while True:
        try:
            salary = float(input("Enter your **total monthly salary/income** (in your currency): "))
            if salary < 0:
                print("Salary cannot be negative. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for your salary.")

    print("\n--- Enter Monthly Expenditures ---")

    # 2. Get Expenses
    expenses = {}
    while True:
        expense_name = input("Enter an **expense category** (e.g., Rent, Groceries, Utilities, or type 'done' to finish): ").strip()
        if expense_name.lower() == 'done':
            break

        while True:
            try:
                expense_amount = float(input(f"Enter the amount spent on **{expense_name}**: "))
                if expense_amount < 0:
                    print("Expense amount cannot be negative. Please enter a valid amount.")
                    continue
                expenses[expense_name] = expense_amount
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for the expense.")

    # 3. Get Taxes Paid
    while True:
        try:
            taxes_paid = float(input("\nEnter the **total taxes** paid for the month: "))
            if taxes_paid < 0:
                print("Taxes paid cannot be negative. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the taxes.")

    # --- Calculations ---
    total_expenses = sum(expenses.values())
    total_outflow = total_expenses + taxes_paid
    final_savings = salary - total_outflow

    # --- Summary Output ---
    print("\n" + "="*40)
    print("  **Monthly Financial Summary** ")
    print("="*40)

    print(f"**1. Total Monthly Income (Salary):** {salary:,.2f}")
    
    print("\n**2. Detailed Monthly Expenditures:**")
    for name, amount in expenses.items():
        print(f"    - {name}: {amount:,.2f}")
    
    print(f"\n**3. Total Monthly Expenses:** {total_expenses:,.2f}")
    print(f"**4. Total Taxes Paid:** {taxes_paid:,.2f}")
    print(f"**5. Total Monthly Outflow (Expenses + Taxes):** {total_outflow:,.2f}")
    
    # 6. Final Savings Calculation
    print("-" * 40)
    print(f"**FINAL MONTHLY SAVINGS:** {final_savings:,.2f}")
    
    if final_savings > 0:
        print(" Congratulations! You saved money this month.")
    elif final_savings < 0:
        print(" Warning: You spent more than you earned this month. You have a deficit.")
    else:
        print(" You broke even this month.")
    
    print("=" * 40)


# Run the program
if __name__ == "__main__":
    financial_keeper()