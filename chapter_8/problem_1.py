# write a program using fuction to find the gretest of three num

def gretest(a,b,c):
    if (a>b and a>c):
        print(a)
    elif(b>a and b>c):
       print(b)
    elif(c>a and c>b):
        print(c)
    

a=int(input("enter the no 1: "))
b=int(input("enter the no 2: "))
c=int(input("enter the no 3: "))
gretest(a,b,c)    