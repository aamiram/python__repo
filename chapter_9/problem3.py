""" write a program to generate the table from 2 to 20 and wriet it to thae different file .
place these file in a folder  for 13 year old """
def generatetable(n):
    table =""
    for i in range(1,11):
        table += f" {n} X {i} = {n*i} \n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range (2,21):
    generatetable(i)