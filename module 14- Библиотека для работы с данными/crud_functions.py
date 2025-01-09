import sqlite3


def connect_(connect):
    connection = sqlite3.connect(connect)
    cursor = connection.cursor()
    return cursor, connection


def disconnect(connection):
    connection.commit()
    connection.close()


def initiate_db():
    cursor, connection = connect_('database.db')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    #for i in range(1, 5):
    #    cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
    #                   (f'Продукт {i}', f'Описание {i}', str(i * 100)))
    disconnect(connection)


def get_all_products():
    cursor, connection = connect_('database.db')
    data = cursor.execute('SELECT * FROM Products')
    return data.fetchall()


def add_user(username, email, age):
    cursor, connection = connect_('database.db')
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    disconnect(connection)


def is_included(username):
    cursor, connection = connect_('database.db')
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is not None:
        return True
    else:
        return False


if __name__ == '__main__':
    initiate_db()
