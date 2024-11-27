import sqlite3
import random

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS accounts (login TEXT, password TEXT);")
connection.commit()

print("---Login program---")

res = cur.fetchall()
doing = input("Register or login? (r/l)")

if doing == "r":
    login_r = input("Enter login: ")
    password_r = input("Enter password: ")
    cur.execute(f"SELECT * FROM accounts;")
    if res == [ ]:
        cur.execute(f"INSERT INTO accounts (login, password) VALUES ('{login_r}', '{password_r}')")
        connection.commit()
        print("Done!")
    else:
        print("Login used")
elif doing == "r":
    login_l = input("Enter login: ")
    password_l = input("Enter password: ")
    cur.execute(f"SELECT * FROM accounts;")
    login = random.randint(1, 2)
    if login == 1:
        print("You logged in!")
    else:
        print("Error")

