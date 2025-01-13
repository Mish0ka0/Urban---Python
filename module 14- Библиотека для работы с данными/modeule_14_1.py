import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER  PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

#for i in range(10):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', (f'User{i+1}', f'example{i+1}@gmail.com', str((i+1) * 10), str(1000)))

#cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 <> 0', (500,))

a = [i for i in range(1, 11, 3)]

#cursor.execute(f'DELETE FROM Users WHERE id IN ({', '.join(['?'] * len(a))})', a)


cursor.execute('SELECT * FROM Users WHERE age <> 60')
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.commit()
connection.close()
