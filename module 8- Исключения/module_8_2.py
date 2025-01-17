def personal_sum(numbers: list):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result += numbers[i]
        except TypeError:
            incorrect_data += 1
            print('Некорректный тип данных для подсчета суммы- ' + numbers[i])
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)
        average = summ[0] / (len(numbers) - summ[1])
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан не корректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
