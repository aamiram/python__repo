# write a class train which has method to book a ticket get statys(no of seat)
# and get fare information of train running under indian railway
from random import randint
class train:
    def __init__(self,trainNO):
        self.trainNo = trainNO

    def book(self,fro,to):
        print(f"ticket is booked in trainno {self.trainNO} from {fro} to {to}")

    def getstatus(self):
        print(f"train no {self.trainNo} is running on time  ")

    def  getfare(self,fro,to): 
       print(f"ticket fare for {self.trainNO} from {fro} to{to} is {randint(30,100)}")

t = train(1299)
t.book("rampur","delhi")
t.getstatus()
t.getfare("rampur","delhi")