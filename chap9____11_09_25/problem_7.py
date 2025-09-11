# write a program to find out the line number where pyhton is present from ques 6

with open("logs.txt","r") as f :
    line  = f.readlines()
    lineno = 1
    for lines in line:
        if("python" in lines):
            print(f"yes python is present \n{lineno}")
            break
        lineno += 1
    else:
        print(f"no pyhton is not  present")



