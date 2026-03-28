def reverse_string():
    text = input("Enter string: ")
    rev = ""
    
    for ch in text:
        rev = ch + rev
    
    print("Reversed:", rev)

reverse_string()