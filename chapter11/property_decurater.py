# the property_decorater is used when you want to give attribute after creating the object

class employee:
    a =  1
    @classmethod
   
    def show (self):
        print(f"the class attribute of a is {self.a}")
    @property  
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e =  employee()
e.a = 45 

e.name = "harry  khan"
print(e.fname,e.lname)
e.show()