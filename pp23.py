def frequency(a, x): 
    count = 0
      
    for i in a: 
        if i == x: count += 1
    return count 
  
# Driver program 
a = ['abs,abc,abc,abc,fdf,jsdlkndabckabcjjgjfabcgfkabclgskabcbnfgoabcjrwgrwabcjhgsabcfndsdfsjfw'] 
x = ['abc']
print(frequency(a, x)) 