# Tip Calculator

# Get input from the user
bill = float(input("Enter the total bill amount: $"))
tip_percent = int(input("Enter the tip percentage you'd like to give (e.g., 10, 15, 20): "))
people = int(input("How many people are splitting the bill? "))

# Calculate tip and total per person
tip_amount = (tip_percent / 100) * bill
total_bill = bill + tip_amount
amount_per_person = total_bill / people

# Display the result
print(f"\nTip Amount: ${tip_amount:.2f}")
print(f"Total Bill (with Tip): ${total_bill:.2f}")
print(f"Each person should pay: ${amount_per_person:.2f}")
