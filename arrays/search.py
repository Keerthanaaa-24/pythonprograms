arr = list(map(int,input("Enter elements:").split()))

key = int(input("Enter element to remove the founded element: "))
new_arr = []
removed= False
for x in arr:
        if x == key and not removed:
                removed = True
                continue
        else:
                new_arr.append(x)
print(new_arr)     
 