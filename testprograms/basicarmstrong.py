n = 1724
org = n
count = len(str(n))
sum = 0

while n>0:
    digit = n%10
    sum =sum + digit**count
    n//=10

if(org==sum):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
    