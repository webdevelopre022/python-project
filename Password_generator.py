#YouTube channel 5starcoder
#subscribe my channel 
#project_03
import random
import string

def generate_password(length=12, use_special=True):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation

    # Ensure password has at least one of each required character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    if use_special:
        password.append(random.choice(string.punctuation))

    password += random.choices(chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(16))
