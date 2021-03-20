# air ticket booking 9/3/2021
def pasngcount(madult , nchild ,dis) :
    fair = (madult*37550) + (nchild*((1/3)*37550))
    tax = 0.07*fair ;
    if (dis == 1  ):
             discount = 0.1*(fair + tax);
    else:
            discount = 678;
    total_cost =  ((fair+tax)-discount);
    return(total_cost)

m= input("Enter number of adults :");
n = input("Enter number of child :");
day = input("Enter weekday :");
day = int(day);
m = float(m);
n = float(n);
amount = pasngcount(m,n , day);
print("total amount is :", amount)
