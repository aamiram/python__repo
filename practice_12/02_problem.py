# write a program to print the third fifth and seventh element from a list using enumerate function

l = [2,3,4,5,6,7,8,8,9]

for i , item in enumerate(l):
    if i == 2 or i ==4 or i ==6 :
        print(item)
