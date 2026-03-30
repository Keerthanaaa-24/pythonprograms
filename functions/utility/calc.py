def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b if b != 0 else "Cannot divide by zero"
    
a = float(input("Enter number:"))
b = float(input("Enter number:"))

print("Addition:",add(a,b))
print("Subtraction:",sub(a,b))
print("Multiplication:",mul(a,b))
print("Division:",div(a,b))