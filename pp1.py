def add_num (data1 , data2):
    result1 = data1+data2;
    return result1;
def sub_num (data1 , data2):
    result2 = data1-data2;
    return result2;
def mul_num (data1 , data2):
    result3 = data1*data2;
    return result3;
def div_num (data1 , data2):
    result4 = data1/data2;
    return result4;
n = input("enter the value:")
m = input("enter the value:")
n = int(n)
m = int (m)
add = add_num(m,n)
print(add)
sub = sub_num(m,n)
print(sub)
mul = mul_num(m,n)
print(mul)
div = div_num(m,n)
print(div)