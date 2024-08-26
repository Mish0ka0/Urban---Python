immatable_var = (17, "Строка", True, [1, 2])
print(immatable_var)
# immatable_var[0] = "Yellow" # кортеж является не изменяемым типоп данных, исключение массив
# он является изменяемым типом внутри кортежа, все остальные типы не изменить
immatable_var[3][0] = 3
print(immatable_var)

mutable_list = [1, 2, "Apple", True, 3, 4, "Banana"]
mutable_list[0] = 17
mutable_list[3] = "False"
print(mutable_list)
