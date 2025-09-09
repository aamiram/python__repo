#  find out that the len of uer name is <10

name = input("enter the user name :")
len= name.__len__()
print(len)
if (len <= 10 )or(len == 10):
    print(" the char is less than 10")
else:
    print("invalid name ")    
    