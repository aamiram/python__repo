# write a program to copy the content from one file to the auther file 
with open("this.txt","r") as f  :
    content =  f.read()

    with open("this_copy","w") as f:
        f.write(content)