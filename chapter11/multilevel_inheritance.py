class employee:
    a = 1 

class programer(employee):

    b = 2 
class manager(programer):
    c =3 


o =employee()
print(o.a)

z = programer()
print(z.b)
print(z.a)

y = manager()
print(y.a)
print(y.c)
print(y.b)
