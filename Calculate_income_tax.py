# Calculate income tax for the given income by adhering to the below rules
# Taxable Income        Rate (in %)
# First Rs.10,0000         0
# Next Rs. 10,0000       10
# The remaining           20

income = int(input("Enter the income:"))
if income <= 100000:
    income_tax = 0
    print("Income tax:",income_tax)

elif income > 100000 and income <= 200000:
    income_tax = (income - 100000) * 0.1
    print("Income tax:",income_tax)

else:
    income_tax = 10000 + (income - 200000) * 0.2
    print("Income tax:",income_tax)