# Email Slicer

# Get user input
email = input("Enter your email address: ")

# Slice the email
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

# Display the result
print(f"Username: {username}")
print(f"Domain: {domain}")
