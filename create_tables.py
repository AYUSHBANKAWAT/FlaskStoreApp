import sqlite3

connections = sqlite3.connect('data.db')
cursor = connections.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text,password text)"
cursor.execute(create_table)

connections.commit()
connections.close()