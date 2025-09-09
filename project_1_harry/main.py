# game of snaik water gun
'''
-1=water
1=snake 
0= gun
'''
import random
computer = random.choice([-1,0,1])
youstr=input("enter your choic ")
youdict={"s":1,"w":-1,"g":0 }
reverse={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]
print(f"you chose {reverse[you]}\ncomputer choice {reverse[computer]}")

if(computer == you):
    print("draw")
else:
    if(computer ==-1 or you ==1):
       print("you winn!")
 
    elif(computer ==1 or you ==0):
       print("you winn!")

    elif(computer ==0 or you ==-1):
       print("you winn!")

    elif(computer ==-1 or you ==0):
        print("you loss!")

    elif(computer ==1 or you ==-1):
       print("you loss!")
    
    elif(computer ==0 or you ==1):
        print("you loss!")
  
    else:
      print("something went wrong")  
    