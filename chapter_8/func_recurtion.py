# recurtion is the a functio which calls its self 
# ex =
# return n *factorial(n-1)
# factorial is calling it self in  a same function 

n=int(input("enter the no "))
def factorial(n):
    
    if(n==1)or (n==0):
        return 1 
    
    return n*factorial(n-1)

print(f"the factorial is {factorial(n)}")

