import sqlite3 
from werkzeug.security import generate_password_hash


db = sqlite3.connect("/home/grace12171/blog.db")

#Drop tables
db.execute("DROP TABLE IF EXISTS posts")
db.execute("DROP TABLE IF EXISTS users")

#Create tables
create_table = "CREATE TABLE posts(author_id INTEGER NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
db.execute(create_table)
create_users_table = "CREATE TABLE users (username TEXT NOT NULL, password TEXT NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
db.execute(create_users_table)

#insert rows into tables
insert_user_stmt = "INSERT INTO users(username, password) VALUES (?, ?)"
db.execute(insert_user_stmt, ("kate", generate_password_hash("password")))
db.execute(insert_user_stmt, ("chris", generate_password_hash("password")))

author_id = db.execute("SELECT rowid FROM users WHERE username=?", ("kate",)).fetchone()[0]
insert_stmt = "INSERT INTO posts (author_id, title, content) VALUES (? , ?, ?)"
db.execute(insert_stmt, (author_id, 'title 1', 'content 1'))
db.execute(insert_stmt, (author_id, 'title 2', 'content 2'))

author_id = db.execute("SELECT rowid FROM users WHERE username=?", ("chris",)).fetchone()[0]
db.execute(insert_stmt, (author_id, 'title 3', 'content 3'))
db.execute(insert_stmt, (author_id, 'title 4', 'content 4'))

results = db.execute("SELECT author_id, title, content FROM posts").fetchall()
for r in results:
    print (r)

results = db.execute("SELECT rowid, username, password FROM users").fetchall()
for r in results:
    print (r)

query = "SELECT username, password, title, content FROM posts JOIN users ON users.rowid = author_id"
db.execute(query).fetchall()
for r in results:
    print(r)

db.commit()
db.close()