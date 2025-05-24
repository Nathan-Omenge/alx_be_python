# Prompting the User for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Displyaing the Results
print("Your monthly savings are: ", monthly_savings)

# Projecting Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Displaying Results
print("Projected savins after one year, with interest, is: ", projected_savings)

