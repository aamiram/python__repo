# repeat program 4 for a list of such i to be exicuted 
an =["how ", "boy", "hope"]
with open("name.txt","r") as f:
    content = f.read()

for A in an :
    content =content.replace(A,"#" *len(A))

with open("name.txt","w") as f :
    f.write(content)
   
