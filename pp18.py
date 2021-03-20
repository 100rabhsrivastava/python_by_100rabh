def getSum(n):  
     
    sum = 0
    while (n != 0):  
        
        sum = sum + (n % 10) 
        n = n//10
        print (n)
    return sum
    
n = int(input())
print(getSum(n))