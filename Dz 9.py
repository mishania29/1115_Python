import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Animal (id INT, name TEXT, type TEXT);")
connection.commit()

cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (1, 'Лев', 'Ссавець');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (2, 'Крокодил', 'Плазун');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (3, 'Орел', 'Птах');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (4, 'Морська черепаха', 'Плазун');")
cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (5, 'Мавпа', 'Ссавець');")
connection.commit()

cur.execute("SELECT * FROM Animal WHERE name='Орел';")
cur.execute(f"UPDATE Animal SET name= 'Сокіл' WHERE name='Орел';")
connection.commit()

cur.execute(f"SELECT * FROM animal;")
res = cur.fetchall()
print(res)

connection.close()