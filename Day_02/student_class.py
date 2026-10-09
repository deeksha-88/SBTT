class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


object1 = Student("John", 20, "male")
ans = object1.name
print(ans)
object1.display()
