import string

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in string.punctuation:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
    if not has_upper:
        print("Password must contain an uppercase letter.")
    if not has_lower:
        print("Password must contain a lowercase letter.")
    if not has_digit:
        print("Password must contain a number.")
    if not has_special:
        print("Password must contain a special character.")