n=int(input("enter the no "))
def factorial(n):
    
    if(n==1)or (n==0):
        return 1 
    
    return n*factorial(n-1)

print(f"the factorial is {factorial(n)}")

