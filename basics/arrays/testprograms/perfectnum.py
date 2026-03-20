nums = [6, 28, 10, 15]
perfect = []
for n in nums:
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s = s + i

    if s == n:
        perfect.append(n)

print(perfect)