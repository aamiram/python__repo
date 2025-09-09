#  how to replace the string from a file 

"""a file contains a word "donkey " multiple time 
you need to write a program which replace this words with #### by updating the same file """

word = "donkey"
with open ("name.txt","r") as f :
    content = f.read()

newcontent = content.replace("donkey" , "#####")    
with open ("name.txt","w") as f :
    f.write(newcontent)