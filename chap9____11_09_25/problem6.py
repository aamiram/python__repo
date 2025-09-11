with open("logs.txt","r") as f :
    content = f.read()
if("pyhton" in content):
    print("yes python is present ")
else:
    print("no python is not present ")
       



