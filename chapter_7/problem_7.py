# write a program to find the factorial of a no 
# 5! = 1x2x3x4x5 fac of 5 
# 3! = 1x2x3  fac of 3

num = int(input("enter the no "))
fac = 1 # whay 1 becouse we have to multiply
for i in range(1,num+1):
    fac = fac*i
print(fac)    

'''
1x1=1
1x2=2
2x3=6
6x4=24 

this is fac of 4
   
'''