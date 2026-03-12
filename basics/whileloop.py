name =input("Enter your name: ")
age=int(input("Enter your age: "))


while name=="":
    name=input("Enter your name: ")

while age < 0:
    print(f"Age cannot be 0")
    age=int(input("Enter your age: "))

print(f"Hey {name}")
print(f"You're {age} years old!")