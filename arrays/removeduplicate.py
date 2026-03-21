nums = [88, 2, 2, 35, 44, 44, 5,88,24]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)