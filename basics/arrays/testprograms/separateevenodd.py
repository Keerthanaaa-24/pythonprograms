nums = [22, 13, 11, 62, 74, 57]
even = []
odd = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Even =", even)
print("Odd =", odd)