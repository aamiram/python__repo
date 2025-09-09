# find out the name is present in a list
name = input("enter the user name :")
len= name.__len__()
print(len)
if (len <= 10 )or(len == 10):
    print(" the char is less than 10")
else:
    print("invalid name ")    
    

list1=["aahan","ali","aayat"]
print(list1)
if name in list1:
    print("yes ")
else:
    print(" name not found")    