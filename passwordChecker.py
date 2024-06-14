import re

def password_strength(password):
    # Check password length
    length = len(password)
    if length < 8:
        return "Password is too short. It should be at least 8 characters."
    
    # Search for lowercase letters
    if not re.search("[a-z]", password):
        return "Password should contain at least one lowercase letter."
    
    # Search for uppercase letters
    if not re.search("[A-Z]", password):
        return "Password should contain at least one uppercase letter."
    
    # Search for digits
    if not re.search("[0-9]", password):
        return "Password should contain at least one digit."
    
    # Search for special characters
    if not re.search("[^a-zA-Z0-9]", password):
        return "Password should contain at least one special character."
    
    # If all checks pass
    return "This is a strong password."

# User input
password = input("Enter a password: ")
print(password_strength(password))
