# write a program to input eight num from the user and display all the unique  num

list_1= []
for i in range(8):
    k = int(input(f"enter the no {i}:"))
    i+1
    list_1.append(k)
print("the unique no are :")

uniq=set(list_1)
for j in uniq:

    print(j)