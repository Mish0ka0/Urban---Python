calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    a = len(string)
    str1 = string.upper()
    str2 = string.lower()
    tuple_ = (a, str1, str2)
    return tuple_


def is_contains(string: str, list_to_search: list):
    count_calls()
    a = -1
    for i in range(len(list_to_search)):
        if string.casefold() == list_to_search[i].casefold():
            a = 1
    if a > 0:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)