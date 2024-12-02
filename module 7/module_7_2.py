def custom_write(file_name, strings: list):
    my_dict = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(len(strings)):
        my_tuple = (i+1, file.tell())
        my_dict.update({my_tuple: strings[i]})
        file.write(strings[i]+'\n')
    file.close()
    return my_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
