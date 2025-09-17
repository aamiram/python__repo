# @staticmethod
class employee:
    language = "python"
    salary = 1200000

    def getinfo(self):
        print(f"the language {self.language} salary {self.salary}")


    @staticmethod
    def wish():
        print("good morning")

harry =  employee()
harry.language= "java"
harry.wish()
harry.getinfo()           