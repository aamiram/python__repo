with open("logs.txt","r") as f :
    content = f.read()
word = " python"    
if ("python" in content):
    print("yes")
else:
    print("no")   
# for w in word:
#     content = content.replace(w,"#"*len(w))     

# with open("logs.txt","w") as f:
#     f.write(content)


