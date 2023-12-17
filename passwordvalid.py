import re

pwd = input("Enter the Password: ")

pwd_len = len(pwd)
is_valid = False

while True:
    if pwd_len < 7 or pwd_len > 20:
        print("Password length must be between 8 and 20 characters.")
        break
    elif not re.search('[A-Z]', pwd):
        print("Password must contain at least one uppercase letter.")
        break
    elif not re.search('[a-z]', pwd):
        print("Password must contain at least one lowercase letter.")
        break
    elif not re.search('[0-9]', pwd):
        print("Password must contain at least one digit.")
        break
    elif not re.search('[#$@!]', pwd):
        print("Password must contain at least one of the special characters: #$@!")
        break
    elif re.search("\s", pwd):
        print("Password must not contain whitespace.")
        break
    else:
        is_valid = True
        break

if is_valid:
    print("Password is valid.")
else:
    print("Password is NOT valid.")
