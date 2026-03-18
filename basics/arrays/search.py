arr = list(map(int,input("Enter elements:").split()))

key = int(input("Enter element to remove the founded element: "))
if key in arr:
        arr.remove(key)
        print("Element found and removed")
else:
        print("Element not found")
print("Array:",arr)