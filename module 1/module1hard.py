grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_students = list(students)    # преобразование множества в список
my_students.sort()              # сортируем список
a = []                          # создаем массив для средних оценок
for i in range(len(grades)):    # добавляем данные в массив
    b = sum(grades[i])
    c = len(grades[i])
    sr: float = b/c
    a.append(sr)
lister = {}                     # создаем словарь
for i in range(len(a)):         # заносим в словарь данные
    lister.update({my_students[i]: a[i]})
print(lister)


