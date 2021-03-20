# temp conversion 
def fanTOdeg(temp):
    result = (temp-32)*(5/9);
    return(result)


t = input("enter temp in F :")
t = float(t)
tem = fanTOdeg(t)
print("temp in degree is : " ,tem)