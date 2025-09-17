class info:
    language = "pyhton"
    salary = 120000

    def func(self):
        print(f"the language {self.language} the salery {self.salary}")


harry = info()
harry.language = "java" 
print(harry.language)
harry.func()       
# info.func(harry) is converted 