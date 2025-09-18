# @classmethod is use to print or take the class instance 
class employee:
    a =  1
    @classmethod
   
    def show (self):
        print(f"the class attribute of a is {self.a}")

e =  employee()
e.a = 45 
e.show()# if there wass no @classmethod then  45 was printed 
# now we mentioned the @classmethod so  the class instance whgich is 1 will be   printed 
# class method is use to directlu use the class instance