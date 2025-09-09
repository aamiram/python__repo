m1=int(input("inter your m1 mark"))
m2=int(input("inter your m2 mark"))
m3=int(input("inter your m3 mark"))

total=m1+m2+m3
p = (total/300)*100
if (p == 90) or (p>=90):
    print("ex")
elif( p == 80) or (p>=80):
    print("A")
elif (p == 70) or (p>=70):
    print("B")
elif (p == 60) or (p>=70):
    print("C")
elif (p <= 50 ):
    print("fail")
