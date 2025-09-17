# __inti__ constrecture
class employe:
    def __init__(self,name,salary,language):
        self.name= name 
        self.salary = salary
        self.language = language


harry = employe("harry",1300000,"javascript")#passing the aurgement for __init__
print(harry.name,harry.salary,harry.language)
        