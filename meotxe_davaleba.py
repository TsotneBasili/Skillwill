class Student:
    university = "Harward"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: [{self.name}], Age: [{self.age}], Grade: [{self.grade}]"

    @property
    def is_passing(self):
        if self.grade > 60:
            return True
        else:
            return False

    def increase_grade(self, add_grade):
        self.grade += add_grade
        return self.grade
