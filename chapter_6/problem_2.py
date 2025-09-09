# write a program to find out the spamin the text 
s1 = "make a lot of money"
s2 = "buy now "
s3 = " subscribe this"
s4 = "click this"

text = input("enter the text: ")
if((s1 in text)or(s2 in text )or(s3 in text)or (s4 in text)):
    print(" the text is sparm:")
else:
    print("the text is not sparm:")    