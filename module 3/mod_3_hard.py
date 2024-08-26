def calculate_structure_sum(name):
    a: int = 0

    for i in name:
        if isinstance(i, list):     # обработка массива
            for j in i:
                if isinstance(j, int):
                    a += j
        if isinstance(i, dict):     # обработка словаря
            dicter = i.items()
            for key, value in dicter:
                a += len(key) + value
        if isinstance(i, tuple):    # обработка кортежа
            for tup in i:
                if isinstance(tup, int):
                    a += tup
                if isinstance(tup, dict):
                    dicter = tup.items()
                    for key, value in dicter:
                        a += len(key) + value
                if isinstance(tup, tuple):
                    a += 0
        if isinstance(i, str):
            a += len(i)

    return a


data_structure = [
    [1, 2, 3],  # 6
    {'a': 4, 'b': 5},  # 11
    (6, {'cube': 7, 'drum': 8}),  # 29
    "Hello",    # 5
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
