def func():
   inch=float(input("enter the no in inches : "))
   
   cm = inch*2.54
   return cm
print(func())


        ############    OR      #############

def func(inch):
    return inch*2.54


n=int(input("enter the no"))
print(f"the value is {func(n)}")

