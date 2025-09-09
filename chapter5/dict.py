marks = {
    "Harry":{"coder":100,"hacker":200},
    "Aamir":5,
    "Rohan":8,
}

print(type(marks),marks.keys())

print("the valueis:",marks["Harry"]["coder"])


# diff between .get and normal print error

print(marks.get("Harry"))#print none 
print(marks["Harry"])# returns an error


