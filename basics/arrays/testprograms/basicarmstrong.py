n = int(input("Enter a number:"))
org = n
sum = 0

while n>0:
    digit = n%10
    sum =sum + digit**3
    n//=10

if(org==sum):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
    