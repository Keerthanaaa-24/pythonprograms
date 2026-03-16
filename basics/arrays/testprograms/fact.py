nums = [5, 4, 6]
fact_nums = []
for n in nums:
    fact = 1

    for i in range(1, n+1):
        fact = fact * i

    fact_nums.append(fact)
print(fact_nums)