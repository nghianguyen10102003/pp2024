class Student:
    def __init__(self,id,name,dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self,course_id,mark):
        self.marks[course_id] = mark

class Course:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_students(self, n):
        for i in range(n):
            id = input("Enter id of student {}: ".format(i + 1))
            name = input("Enter name of student {}: ".format(i + 1))
            dob = input("Enter date of birth of student {}: ".format(i + 1))
            student = Student(id, name, dob)
            self.add_student(student)

    def input_courses(self, m):
        for i in range(m):
            id = input("Enter the id of course {}: ".format(i + 1))
            name = input("Enter the name of course {}: ".format(i + 1))
            course = Course(id, name)
            self.add_course(course)

    def add_mark(self, student_id, course_id):
        for student in self.students:
            if student.id == student_id:
                mark = input("Enter the mark for student {} in course {}: ".format(student_id, course_id))
                student.add_mark(course_id, mark)
                print("Mark added successfully!")
                return
        print("Student ID not found!")

    def print_students(self):
        for student in self.students:
            print("Student ID:", student.id)
            print("Name:", student.name)
            print("Date of Birth:", student.dob)

    def print_courses(self):
        for course in self.courses:
            print("Course ID:",course.id)
            print("Name:",course.name)

    def print_marks_for_course(self,course_id):
        for student in self.students:
            if course_id in student.marks:
                print("Student ID:",student.id)
                print("Mark:",student.marks[course_id])
            else:
                print("Student ID:",student.id)
                print("Mark: Not available")

school = School()

n = int(input("Enter the number of students: "))
school.input_students(n)

m = int(input("Enter the number of courses: "))
school.input_courses(m)

while True:
    print("Do you want to add mark? (1 is yes / 0 is no)")
    choice = int(input())
    if choice == 1:
        student_id = input("Enter the id of student: ")
        course_id = input("Enter the id of course: ")
        school.add_mark(student_id,course_id)
    else:
        break

print("\nList of students:")
school.print_students()

print("\nList of courses:")
school.print_courses()

course_id = input("Enter the id of course you want to check marks for: ")
print("\nMarks for course {}:".format(course_id))
school.print_marks_for_course(course_id)