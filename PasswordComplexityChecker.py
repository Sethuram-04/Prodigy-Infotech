import re

def check_password_strength(password):

    # Check password length
    if len(password) < 8:
        return "Weak"

    # Check for uppercase, lowercase, numbers, and special characters
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_number = re.search(r'\d', password)
    has_special_char = re.search(r'[!@#$%^&*()_+\-\=\[\]{};\':\\|,.<>/?]', password)

    if not (has_uppercase and has_lowercase and has_number and has_special_char):
        return "Medium"

    return "Strong"

# Get user input for the password
password = input("Enter your password: ")

# Check password strength
strength = check_password_strength(password)

# Provide feedback to the user
print("Password strength:", strength)