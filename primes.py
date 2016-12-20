primes =  [2]
numbers = list(range(3,30))
for num in numbers:
    for prime in primes:
        if num % prime == 0:
            break
    else:
        primes.append(num)

print(primes)

