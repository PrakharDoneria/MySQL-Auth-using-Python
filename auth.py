import os
import mysql.connector as con
import ui

# Connect to the database
db = con.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), passwd=os.getenv("DB_PASSWORD"), database=os.getenv("DB_DATABASE"))
cur = db.cursor()

# Make LOGIN
def login(email, password):
    if email == "" or password == "":
        ui.colorRed("Please enter all the fields")
        return False
    else:
        try:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cur.fetchone()
            if user is None:
                ui.colorRed("User does not exist")
                return False
              
            elif user[2] != password:
                ui.colorRed("Incorrect password")
                return False
            else:
                return True
        except Exception as e:
            return "An error occurred: " + str(e)


# Make NEW account
def signup(username, email, password):
    if username == "" or email == "" or password == "":
        ui.colorRed("Please enter all the fields")
        return False
    else:
        # User input validation
        try:
            if len(password) < 8:
                ui.colorRed("Password must be at least 8 characters")
                return False
            elif "@" not in email or "." not in email:
                ui.colorRed("Please enter a valid email")
                return False
            else:
                # Check if the user already exists
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                if cur.fetchone():
                    ui.colorRed("User already exists with this email")
                    return False
                else:
                    cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
                    db.commit() 
                    return "Account created successfully"
        except Exception as e:
            return "An error occurred: " + str(e)

# Delete user
def deleteUser(username, email, password):
  if username == "" or email == "" or password == "":
    ui.colorRed("Please enter all the fields")
    return False
  else:
    try:
      cur.execute("SELECT * FROM users WHERE email = %s", (email,))
      user = cur.fetchone()
      if user is None:
        ui.colorRed("User does not exist")
        return False
      elif user[2] != password:
        ui.colorRed("Incorrect password")
        return False
      else:
        cur.execute("DELETE FROM users WHERE email = %s", (email,))
        db.commit()
        ui.colorGreen("Account deleted successfully")
    except Exception as e:
        ui.colorRed(e)