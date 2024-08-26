def number(n):
    if n == 0:
        return 0
    else:
        return n % 10 + number(n // 10)


def numeric():
    for i in range(1000):
        a = number(i)
        if i % 3 == 0 and i % 5 != 0 and a < 10:
            print(i)


numeric()
