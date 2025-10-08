#write a program to open  three file 1.txt , 2.txt , 3.txt 
# if any these file are not present a  massage without exiting the program must be printed propting the same 

try:
     with open("1.txt", "r") as f:
       print(f.read())

except Exception as e:
     print(e)

try:
     with open ("2.txt" , "r") as f :
      print(f.read())

except Exception as e:
    print(e)    

try:
    with open ("3.txt" , "r") as f:
      print(f.read())

except Exception as e:
    print(e)

print("thank you")    


