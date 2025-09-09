"""write a program to read the text from a given file "poem.txt"
and find out whether the content is presentin the file or not 
"twinkel"
"""


# with open("poem.txt","r")as f: #Here, f is a file object, not the file’s content.
#   content=f.read()  # read the whole file into a string(content)
    
#   if("twinkel " in content ):
#     print("yes")
#   else:
#     print("no")    


f=open("poem.txt","r")

content = f.read()

if ("twinkel " in content):
       
       print("yes")
else:
        
        print("no") 

f.close()