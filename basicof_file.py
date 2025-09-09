# how to write in a file 
with open("demo.txt","w") as f:
    f.write("hellow ,this is the first line \n")

# how to read the fiel 
with open("demo.txt","r") as f:
    content = f.read()
    print("file content after writing :\n\n",content) 
print(" \n ")

# how to append the file 
with open("demo.txt","a") as f :
    f.write("This line is append \n") 

#  for checking the append line 
with open("demo.txt","r") as f:
    cont = f.read()
    print(f"the file after apprnding{cont}") 