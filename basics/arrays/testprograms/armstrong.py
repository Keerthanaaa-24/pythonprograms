nums = [153, 370, 371, 407, 120, 10]
armstrong = []
for n in nums:
    temp = n
    count = 0

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** count
        temp = temp // 10

    if total == n:
        armstrong.append(n)

print(armstrong)
