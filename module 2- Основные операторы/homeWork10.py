numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in numbers:
    is_prime = bool
    if i == 1:
        continue
    if i == 2:
        primes.append(i)
        continue
    for j in range(2, i):
        if i % j != 0:
            is_prime = True
        else:
            is_prime = False
            break
    if is_prime == 1:
        primes.append(i)
    else:
        not_primes.append(i)
print("Primes: ", primes)
print("Not Primes: ", not_primes)
