numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
    if i not in not_primes:
        primes.append(i)
print("Primes: ", primes)
print("Not_primes: ", not_primes)
