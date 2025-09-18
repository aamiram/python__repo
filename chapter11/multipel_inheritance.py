class employee:
    company = "ITC"
    name = "default"
    def show(self):
        name = "aamir"
        print(f"the name of the employe is {name} and comp {self.company}")
          
class coder:
    language =  "python"
    def printlanguage(self):
        print(f"the language is {self.language}")


class programmer(employee,coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}language")

a= employee()
b = programmer()
b.show()
b.printlanguage()
b.showlanguage()