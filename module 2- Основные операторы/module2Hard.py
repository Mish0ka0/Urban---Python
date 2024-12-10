import random


def decoder_(a):
    kod = ''
    for i in range(1, (a+1)//2):
        for j in range(1, a):
            if a % (i + j) == 0 and i < j:
                kod = kod + str(i) + str(j)
    return kod


randomValue = random.randint(3, 20)
decoding = decoder_(randomValue)
print(f'Шифр {randomValue}')
print(f'Пароль к шифру: {decoding}')
