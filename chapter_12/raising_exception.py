a= int (input("enter a no  "))
b =  int(input ("enter second no "))

if(b== 0 ):
    raise ZeroDivisionError ("no can not be divided by 0")
else:
   print(f" the division a/b is {a/b} ")