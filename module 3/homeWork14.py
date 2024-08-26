def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print()

value_list = [1, 'str', (3, 4, 5)]
value_dict = {'a': 5, 'b': False, 'c': [1, 2]}
print_params(*value_list)
print_params(**value_dict)
print()
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
