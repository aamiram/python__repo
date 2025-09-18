#  if you want to access the constructer of paarent class only from the child class 
# just use the   def __init__(self):
                    #  super().__init__()

class employee:
    def __init__(self):
        print("constructer of employe")
    a = 1 

class programer(employee):
    def __init__(self):
        super().__init__()
        print("constructer of programer")


    b = 2 
class manager(programer):
    def __init__(self):
        super().__init__()
        print("constrcter of manager ")
    c =3 


# o =employee()
# print(o.a)

# z = programer()
# print(z.b)
# print(z.a)

y = manager()
print(y.a)
print(y.c)
print(y.b)
