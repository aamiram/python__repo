# repeat program 4 for a list of such i to be exicuted 
an =["how ", "boy", "hope"]
with open("name.txt","r") as f:
    content = f.read()
for a in an :
    content = content.replace(a,"*"*len(a))
with open("name.txt","w") as f :
    f.write(content)        
    # for w in word:
#     content = content.replace(w,"#"*len(w))     

# with open("logs.txt","w") as f:
#     f.write(content)
