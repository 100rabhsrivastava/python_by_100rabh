from array import *

a1 = array('i', ())


n= int(input("enter length of array"))

for i in range(n):
    # x= int(input("enter  array value :"))
    a1.append(n-i)

print(a1)
temp =0
for k in range(n):
    if (a1[k] > a1[n-k]):
        temp = a1[k]
        a1[k] = a1[n-k]
        a1[n-k] = temp
    else:
        print("no-think")

print(a1)


# val = int(input("enter value :"))
# k =0
# for e in range(n):
#     if val == a1[e]:
#         k+=1




# print(k)



