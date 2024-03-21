import ui

# Checks if input is valid
def isValidStr(input):
    if isinstance(input, str):
        return True
    else:
        print("Input must be a string.")
        return False

# Checks if password is strong
def isValidPass(input):
    if len(input) < 8:
        print("Password must be at least 8 characters long.")
        return False
    elif " " in input:
        print("Password cannot contain spaces.")
        return False
    elif input.isalnum():
        print("Password must contain at least one non-alphanumeric character.")
        return False
    else:
        return True

# Checks if email is valid
def isValidEmail(input_email):
    if len(input_email) < 6:
        print("Email length must be at least 6 characters.")
        return False
    elif "@" not in input_email or "." not in input_email:
        print("Email must contain '@' and '.' symbols.")
        return False
    elif input_email.count("@") != 1:
        print("Email must contain exactly one '@' symbol.")
        return False
    elif input_email.count(".") == 0:
        print("Email must contain at least one '.' symbol.")
        return False
    else:
        return True
