class Student:

    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def hello(self):
        print(" Hello Guy's I'm"+ " " + self.first_name)

    def feedback(self):
        print(f"The sessions were insightful that is why I achieved a grade of {self.grade}")


        # Decorator - it is a callable function that takes another function or method as an argument 
        # @classmethod - it defines methods that operate on the class itself
    @classmethod
    def change_grade(cls, student, grade_delta):
        student.grade += grade_delta
        return student.grade














# student_one = Student()
# print(student_one)
