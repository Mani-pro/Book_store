import sqlite3


def connect():
    connection = sqlite3.connect("./book.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY , title TEXT , author TEXT , year INTEGER , isbn INTEGER)""")
    connection.commit()
    connection.close()


def insert(titel, author, year, isbn):
    connection = sqlite3.connect("./book.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO books VALUES (NULL , ? , ? , ? , ?)""",
                   (titel, author, year, isbn))
    connection.commit()
    connection.close()


def view_all():
    connection = sqlite3.connect("./book.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM books""")
    books = cursor.fetchall()
    connection.close()
    return books


def search(title="", writer="", year="", isbn=""):
    connect = sqlite3.connect("./book.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ? OR Writer = ? OR year = ? OR ISBN = ?",
                   (title, writer, year, isbn))
    books = cursor.fetchall()
    connect.close()
    return books


def delete(id):
    connection = sqlite3.connect("./book.db")
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM books WHERE id = ?""", (id, ))
    connection.commit()
    connection.close()


def update(id, title, writer, year, isbn):
    connect = sqlite3.connect("./book.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE books SET title = ?, Writer = ?, year = ?, ISBN = ? WHERE id = ? ",
                   (title, writer, year, isbn, id))
    connect.commit()
    connect.close()


connect()
