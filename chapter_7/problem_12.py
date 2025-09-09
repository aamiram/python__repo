#  program for printing the table in reverse
n =int (input("enter the no :"))

for i in range(10,0,-1):
    b=n*i
   
    print(f"{n} X {i} = {b}")

    '''
    or 

    n=int(input("enter the no : "))

    for i in range(1,11):
        print(f"{n} X {11-i} = {n*(11-i)} ")

    '''
