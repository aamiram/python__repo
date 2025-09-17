# __init__ the method which is start with underscore __ is called as dunder method 
class employe:
    language = "python"
    salary = 1200000


    def __init__(self):#dunder method(starts with__)
        print("creating an boject")#called automaticaly
    
    def getinfo(self):
        print(f"language is {self.language}")

    @staticmethod
    def great():
        print("good morning")

harry =  employe()
# harry.getinfo()
# harry.great()
harry.name ="aamir"
print(harry.name, harry.language)

            