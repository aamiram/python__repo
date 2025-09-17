class  emplpoye:
    language =  "python"
    salary = 120000 


harry = emplpoye
harry.language = "java"
print(harry.language,harry.salary)    
# the  instance attribute java will be print 
# becouse the instance attribute take preference up on the class attribute

