from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

# Input date of birth
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert to datetime object
try:
    birthdate = datetime.strptime(dob_input, "%Y-%m-%d")
    age = calculate_age(birthdate)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
  
