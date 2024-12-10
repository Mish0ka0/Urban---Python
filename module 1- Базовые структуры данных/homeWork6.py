my_dict = {"Alex": 1997, "Olaf": 2001, "Christof": 1995}
print("Словарь", my_dict)
print("Значение по ключу:", my_dict.get("Alex"))
print("Такого значения нет:", my_dict.get("Anna",))
my_dict.update({"Sasha": 2005, "Eva": 1992})
print("Обновленный словарь:", my_dict)
print("Удаленное значение:", my_dict.pop("Olaf"))
print("Обновленный словарь:", my_dict)

my_set = {1, 2, 2, 2, 3, 4, 4, 4, True, True, "string", (2, 3, 4)}
print("Новое множество:", my_set)
my_set.add("apple")
my_set.add(9)
my_set.discard(3)
print("Обновленное множество:", my_set)
