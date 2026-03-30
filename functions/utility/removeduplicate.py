def remove_duplicates():
    lst = list(map(int, input("Enter numbers: ").split()))
    unique = []

    for i in lst:
        if i not in unique:
            unique.append(i)

    print("Without duplicates:", unique)

remove_duplicates()