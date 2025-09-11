# write a program to find out whether 
# the file is identical & matches the content of anouther file 

with open("file1.txt", "r") as f:
    content = f.read()
with open("file2.txt","r") as f :
    con = f.read()

if (content == con):
        print("yes the file are same ")
else:
        print("the file are not same ")

