def calculate_structure_sum(name):
    a: int = 0

    if isinstance(name, list):  # обработка списка
        for i in range(0, len(name)):
            a += calculate_structure_sum(name[i])

    if isinstance(name, dict):  # обработка словаря
        dicter = name.items()
        for key, value in dicter:
            a += len(key) + value

    if isinstance(name, tuple):  # обработка кортежа
        for tup in name:
            a += calculate_structure_sum(tup)

    if isinstance(name, set):
        for i in name:
            a += calculate_structure_sum(i)

    if isinstance(name, int):
        a += name

    if isinstance(name, str):
        a += len(name)

    return a


data_structure = [
    [1, 2, 3],  # 6
    {'a': 4, 'b': 5},  # 11
    (6, {'cube': 7, 'drum': 8}),  # 29
    "Hello",  # 5
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
