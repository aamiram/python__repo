# creat a class with a class attribute "a" create an object from it 
# and set "a" directly using object a=0 and does this change the class attribute
class demo:
    a=4 #class argument a = 4 
o= demo()  #object from a class
print(o.a)
o.a =0#set a directly using object a=0 
print(o.a)
# does this change the class attribute (no)