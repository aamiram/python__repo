# # pyhton function to print the multiplication table
def table():
    a=int(input("enter the no "))  
    for i in  range(1,11):
        m=a*i
        
        print(f"{a} X {i} = {m}")  

 
table()  

