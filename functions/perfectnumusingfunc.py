def perf_num(n):
    sum_div=0 #should store the sum so starts as 0
    for i in range(1,n//2+1): #takes numbers from 1 to n//2 and includes n//2
        if n%i==0: #divides i by n(remainder should be 0)
            sum_div=sum_div+i #sums with the divisors
    s = (sum_div==n) #checks the condition if true or false
    return s #returns either true or false

n = int(input("Enter a Number:"))
result = perf_num(n) #calls function and stores result
if result: #if result is true
    print("It is a Perfect number")
else: #else the result is false
    print("It is NOT a Perfect Number")
