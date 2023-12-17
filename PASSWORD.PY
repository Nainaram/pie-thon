import re

def is_valid_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r"\d", password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):
        return False
    
    # If all conditions are met, the password is considered valid
    return True

# Example usage
password_to_check = input("Enter the password to check: ")

if is_valid_password(password_to_check):
    print("The password is valid.")
else:
    print("The password is not valid.")
