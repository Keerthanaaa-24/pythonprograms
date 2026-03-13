n = int(input("Enter limit: "))
even = 0
odd = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print("Sum of Even numbers =", even)
print("Sum of Odd numbers =", odd)