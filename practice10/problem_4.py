#  add a static method in problem 2 to greet the user with hello
class calculater :
    def __init__(self,n):
        self.n=  n 
    def square(self):
        print(self.n*self.n)  

    def cube(self):
        print(self.n*self.n*self.n)  

    def squareroot(self):
        print(self.n**0.5)  
    @staticmethod
    def great():
        print("good morning")

c=calculater(4)
c.great()
c.square()
c.cube()
c.squareroot()

             
      