from array import *
vals = array( 'i' ,[1,2,3,4,5,6,7,8])
print(vals)
# for i in range(3):
#     while(i<7):
#         f = i+1
#         print(vals[f] , end = " ")
#         i = i+1;
#     print("\n")
# m = number of shift 
# n = size of array 
# e =  incremental integer 
g=0
while(g<4):
    for e in range (8):
        f = 0;
      #number of shift 
        if (e<=(7-g)):
            
            f= e+g
            print(vals[f] , end = " ")
        else:
            f= 0+g
            print(vals[f] , end = " ")
            e=e+1
    
    g= g+1
    print("\n");
   






    
    


