class Student:
    def __init__(self, name, rollnumber, grade):
        self.name = name
        self.rollnumber = rollnumber
        self.grade = grade

    def show_name(self):
        print("Name of the student is " + self.name)

    def show_rollnumber(self):
        print("Roll number is " + str(self.rollnumber))

    def show_grade(self):
        
        print(f"Grade of the student {self.name} is {self.grade}")


x = Student("Sreekanth", 18, "A")
x.show_name()
x.show_rollnumber()
x.show_grade()

class     