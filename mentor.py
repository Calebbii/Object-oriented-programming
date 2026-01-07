class Mentor:

    def __init__(self,name):

        self.name = name
        self.students = [] # many students
    
    def assign_students(self,student):
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student.first_name)