nums = [1, 2, 2, 3, 3, 3,4,4,4,6,7,5,6,7,6,7,8,9,2,1,3]
freq = {}
for n in nums:
    if n in freq:
        freq[n] = freq[n] + 1
    else:
        freq[n] = 1
print(freq)
