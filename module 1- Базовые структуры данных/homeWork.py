# "1st program".

print(9 ** 0.5)
print((9 ** 0.5) * 5)

# "2nd program".

print(9.99 > 9.98 and 1000 != 1000.1)

# "3rd program".

a = (1234 % 1000) // 10
b = (5678 % 1000) // 10
print(a+b)

# "4th program".

a = 13.42
a1 = int(a)  # целое число, числа a
a2 = int(a*100)
a3 = a2 % 100  # дробную часть, числа a
b = 42.13
b1 = int(b)  # целое число, числа b
b2 = int(b*100)
b3 = b2 % 100  # дробную часть, числа b
print(a1 == b3 or b1 == a3)
