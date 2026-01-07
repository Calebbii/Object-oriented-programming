from student import Student
from mentor import Mentor
# OOP - Object oriented programming

# Object - An object is a bundle of related attributes(Variables) and methods(functions)

# Class - is a blueprint that is used to create objects
#       - data + functions


# Creating our student objects
student_one = Student("Jeff", "Muna", 98)
student_two = Student("Taran", "Chase", 91)

student_three = Student("Tim", "Mulata", 91)
student_4 = Student("Susan", "Maina", 91)

print(student_one.first_name)
print(student_two.last_name)

student_one.hello()
student_one.feedback()

student_two.hello()
student_two.feedback()

# Changing the grades
Student.change_grade(student_one, -6)
Student.change_grade(student_two, 5)


# Printing the updated grade
print(f"{student_one.first_name}'s new grade is :{student_one.grade}")
print(f"{student_two.first_name}'s new grade is :{student_two.grade}")

# Object Relationships
# One to many relationship - When one object is associated with many other objects

# Many to Many relationship - Many objects of one class related to many objects of another class

# Mentor class
# One mentor -> many students

# Creating a Mentor
mentor_one = Mentor("Caleb")
mentor_two = Mentor("Julius")

print(mentor_one.name)

# Assigning students to our mentor
mentor_one.assign_students(student_one)
mentor_one.assign_students(student_two)

mentor_two.assign_students(student_three)
mentor_two.assign_students(student_4)

# mentor_one.list_students()
mentor_two.list_students()

# Many to Many relationship
# Todo

# Create a book(languages) Class
# A student can have many books
# The books can be owned by many students
# Both classes should maintain a reference to each other

# Create a Course Class
# A student can take many courses
# A certain course can be taken by many students
# Both classes should maintain a reference to each other