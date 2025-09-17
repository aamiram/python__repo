class Student:
    def marks(self, m1, m2, m3):
        total = m1 + m2 + m3
        average = total / 3
        print("Total:", total)
        print("Average:", average)

# Create object
s1 = Student()
s1.marks(85, 90, 80)
