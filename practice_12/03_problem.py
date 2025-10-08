#  write a list comprehension to print a  list which print the multiplication table of a user intered number

n =  int(input("enter a no : "))


table  = [n*i for i  in range (1,11)]
print(table) 

