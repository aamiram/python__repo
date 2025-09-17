# write a class "calculater" capaible of finding square , cube and square root of a number
class calculater:
    # def __init__(self,n):
    #     self.n= n 
    # def square(self):
    #     print(f"the square is {self.n*self.n}")
    #     print(f"cube= {self.n*self.n*self.n}")
    #     print(f"square root {self.n**0.5}")
#    or   #
    def square(self,n):
        print(f"square{n*n}")
        print(f"cube{n*n*n}")
        print(f"square root{n**0.5}")



a = calculater()      
a.square(4)
