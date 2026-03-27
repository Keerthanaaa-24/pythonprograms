def find_largest():
    lst = list(map(int, input("Enter numbers: ").split()))
    
    largest = lst[0]
    
    for i in lst:
        if i > largest:
            largest = i
    
    print("Largest number:", largest)

find_largest()
