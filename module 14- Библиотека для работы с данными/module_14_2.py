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

#for i in range(10):
#    if (i + 1) % 2 != 0:
#        cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i + 1))
a = 1
#for i in range(10):
#    cursor.execute('DELETE FROM Users WHERE id = ?', (i + a,))
#    a += 2

#cursor.execute('SELECT * FROM Users')
#users = cursor.fetchall()

#for user in users:
#    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute('DELETE FROM Users Where id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
print(all_balance / total_users)

#connection.commit()
connection.close()