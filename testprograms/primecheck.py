nums = [2, 33, 15, 13, 7, 9, 24]
primes = []
for n in nums:
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        primes.append(n)

print(primes)