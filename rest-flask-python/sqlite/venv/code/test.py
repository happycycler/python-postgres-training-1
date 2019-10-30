import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id integer primary key autoincrement, username text, password text)"
cursor.execute(create_table)

user = (1, 'mrprice', 'password')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

user = [
    (2, 'blprice', 'password'),
    (3, 'adprice', 'password')
]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, user)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row[0])

connection.commit()
connection.close()