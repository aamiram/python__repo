# 1st

print(open("file_plain.txt").read())  
# 
#  this is write and short way to do it 


# 2nd
f=open("file_plain.txt","r")
data = f.read()
print(data)
f.close


# the three main thing to read the data from file is to open file read the data and print the reeden data 




# 3rd method
with open("file_plain.txt","r")as f:
    print(f.read())