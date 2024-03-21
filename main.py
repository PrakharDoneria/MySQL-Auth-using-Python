import os
import ui
import helpers
import auth
import mysql.connector as con

# Connect to the database
db = con.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), passwd=os.getenv("DB_PASSWORD"), database=os.getenv("DB_DATABASE"))
cur = db.cursor()

# Table Creation
try:
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, email VARCHAR(50), password VARCHAR(50))")
except Exception as e:
    print(e)

# Display welcome message
ui.colorBlue("========================================\n\n")
print("===== WELCOME PLEASE LOGIN/REGISTER =====\n\n")
print("1. Create a new account \n2. Login to your account\n3. Delete my account \n\n")
option = input("Enter your option: ")

try:
    option = int(option)
    if option not in [1, 2, 3]:
        raise ValueError
except ValueError:
    ui.colorRed("Invalid option. Please enter 1, 2 or 3.")
    exit()

ui.colorBlue("\n\n========================================\n\n")

# Register/Login user
if option == 1:
    username = input("Enter your username: ")
    if not helpers.isValidStr(username):
        ui.colorRed("Invalid username format. Please enter a valid username.")
        exit()

    email = input("Enter your email: ")
    if not helpers.isValidEmail(email):
        ui.colorRed("Invalid email format. Please enter a valid email.")
        exit()

    password = input("Enter your password: ")
    if not helpers.isValidPass(password):
        ui.colorRed("Invalid password format. Please enter a valid password with alphabet, number and specific symbols.")
        exit()

    success = auth.signup(username, email, password)
    if success == True:
        ui.colorGreen("Welcome to the community. Account Created successfully")
        ui.clear()
    else:
        ui.colorRed(success)

elif option == 2:
    email = input("Enter your email: ")
    if not helpers.isValidEmail(email):
        ui.colorRed("Invalid email format. Please enter a valid email.")
        exit()

    password = input("Enter your password: ")
    if not helpers.isValidPass(password):
        ui.colorRed("Invalid password format. Please enter a valid password with alphabet, number and specific symbols.")
        exit()

    success = auth.login(email, password)
    if success == True:
        ui.colorGreen("Logged in successfully")
        ui.clear()
    else:
        ui.colorRed(success)

#Delete account
elif option == 3:
  ui.clear()
  email = input("Enter your email: ")
  if helpers.isValidEmail(email):
    password = input("Enter your password: ")
    if helpers.isValidPass(password):
      username = input("Enter your username: ")
      if helpers.isValidStr(username):
        print("\n\n")
        ui.colorRed("=== PLEASE WRITE CONFIRMATION MESSAGE ===")
        print("\n\n")
        print("Write this message 'I CONFIRM TO DELETE MY ACCOUNT '\n :")
        message = input()
        if message.upper() == "I CONFIRM TO DELETE MY ACCOUNT":
          auth.deleteUser(username, email, password)
        else:
          print("Wrong Input")