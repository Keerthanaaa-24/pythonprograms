nums = [123, 456, 789]
result = []
for n in nums:
    temp = n 
    s = 0

    while temp > 0:
        digit = temp % 10 #separate the number
        s = s + digit #add each digit to the next
        temp = temp // 10 #removes the last digit

    result.append(s)
print(result)