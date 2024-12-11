def is_prime(func):
    def wrapper(*args):
        argument = func(*args)
        if argument % 2 != 0 and argument % 3 != 0:
            print('Простое')
        else:
            print('Составное')
        return argument
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
