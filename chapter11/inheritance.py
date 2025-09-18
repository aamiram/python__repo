class employe:
    company = "ITC"
    name= " sahil"
    def show(self):
        print(f"the name is {self.name}and salery is {self.company}")

    
    
# class programer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name}and salery is {self.saery}")

#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")   
    
# insted of this 

class programer(employe):
    company= "ITC infotech"
    language = "pyhton"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")   
    
        
a = employe()  
b= programer()
print(a.company, b.company)      