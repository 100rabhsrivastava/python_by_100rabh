from array import *
arr = array('i', ())

n = int(input("enter the length of array"))

for i in range(n):
    x = int(input("enter the length of array"))
    arr.append(x)
print(arr)

val = int(input("enter the value"))
for k in range(n):
    if (val == arr[k]):
       print(" value is at :" ,k )
# else:
#     print("no value")
        
        
        
#         if val == arr[k]:
#         print("the value is at :", k)
# else:
#     print("value is not in array")
# )
