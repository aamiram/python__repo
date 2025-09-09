f=open("my_file.txt","r")

line=f.readline()
while (line != " "):
    print(line)
    line= f.readline()

f.close
