"""the game function in a program lets a user play a game and return the score  as an intiger .
you need to read a file       hiscore.txt" which is either blank or contains the previous hi score .
you need to write a program to update the      hiscore whenevr the game()function breaks the      hiscore
 """
import random
def game():
    print("you are playing a game :")
    score =  random.randint(1,56)
    
    with open("hiscore.txt") as f :# if teh file is empty then data is 0 
        hiscore = f.read()# and if file is not empty then give a int value 
    if (hiscore != ""):
           hiscore = int(hiscore)
    else:
           hiscore = 0 
    print(f"score is {score}")
    if(score > hiscore):
        with open("hiscore.txt","w") as f :
            f.write(str (score ))
    return score 
game()        


