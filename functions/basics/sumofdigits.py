def sum_of_digits():
    num = int(input("Enter a number: "))
    total = 0
    
    while num > 0:
        total += num % 10
        num = num // 10
    
    print("Sum of digits:", total)

sum_of_digits()