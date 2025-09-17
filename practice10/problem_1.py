# create a class "programmer" for storing information of few programmers working at microsoft
class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name 
        self.salary =  salary
        self.pin =  pin

          
p = programmer("harry",1200000,245001)       
print(p.name,p.salary, p.salary,p.company)
r = programmer("rohan",130000,245002)
print(r.name,r.salary,r.pin,r.company)