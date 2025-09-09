with open("a.txt", "r") as f1, open("b.txt", "w") as f2:
    data = f1.read()
    f2.write(data)

print("content is  copied succes fully")    