class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def total(self):
        self.total=self.mark1+self.mark2+self.mark3
        print(f"Total marks: {self.total}")
    def average(self):
        self.average=(self.mark1+self.mark2+self.mark3)/3
        print(f"Average marks: {self.average}")
    def grade(self):
        if self.average>=90:
            print("Grade: A")
        elif 90>self.average>=80:
            print("Grade: B")
        elif 80>self.average>=60:
            print("Grade: C")
        else:
            print("Grade: F")
student1=Student("Name1",12,99,81,90)
student1.total()
student1.average()
student1.grade()

