import math
class Student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        self.mark={}
        self.gpa = None

    def add_mark(self,course_id,mark):
        self.mark[course_id] = mark

class Course:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class School:
    def __init__(self):
        self.students=[]
        self.courses=[]
    
    def input_s(self,n):
        for i in range(n):
            id=input("Enter id of student {} :".format(i+1))
            name=input("Enter name of student {} :".format(i+1))
            dob=input("Enter date of birth of student {} :".format(i+1))
            s = Student(id,name,dob)
            self.students.append(s)
    
    def input_c(self,m):
        for i in range(m):
            id=input("Enter id of course {} :".format(i+1))
            name=input("Enter name of course {} :".format(i+1))
            c = Course(id,name)
            self.courses.append(c)
    
    def input_mark(self,s_id,c_id):
        for s in self.students:
            if s.id==s_id:
                mark=input("Enter the mark of student have id {}".format(s.id))
                marks=math.floor(int(mark))
                s.add_mark(c_id,marks)
                return
    
    def print_s(self):
        for s in self.students:
            print("Student id:{},name:{},date of birth:{}".format(s.id,s.name,s.dob))
    
    def print_c(self):
        for c in self.courses:
            print("Course id:{},name:{}".format(c.id,c.name))
    
    def print_m(self,c_id):
        print("Mark of course id {}:".format(c_id))
        for s in self.students:
            if c_id in s.mark:
                print("Student id :{},mark :{}".format(s.id,s.mark[c_id]))
    
    def cal_aver_of_one(self,s_id):
        sum_mark=0
        count=0
        for s in self.students:
            if s_id in s.id:
                for c in self.courses:
                    if c.id in s.mark:
                        count+=1
                        sum_mark =sum_mark+s.mark[c.id]
        return sum_mark/count
    
    def sort_s_l_gpa(self):
        arr={}
        for s in self.students:
            s.gpa=self.cal_aver_of_one(s.id)
        for s in self.students:
            i=0
            arr[i]=s.gpa
            i+=1
        arr.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(self.student)):
            for s in self.students:
                if s.gpa == arr[i]:
                    print("Id student:{},Name student:{},Date of birth{},GPA:{}".format(s.id,s.name,s.dob,s.gpa))

school = School()

n = int(input("Enter the number of students: "))
school.input_s(n)

m = int(input("Enter the number of courses: "))
school.input_c(m)

while True:
    print("Do you want to add mark? (1 is yes / 0 is no)")
    choice = int(input())
    if choice == 1:
        student_id = input("Enter the id of student: ")
        course_id = input("Enter the id of course: ")
        school.input_mark(student_id,course_id)
    else:
        break

print("\nList of students:")
school.print_s()

print("\nList of courses:")
school.print_c()

course_id = input("Enter the id of course you want to check marks for: ")
school.print_m(course_id)

cal_id=input("Enter your id student you want to calculate the GPA:")
print("Student id :{},GPA: {}".format(cal_id,school.cal_aver_of_one(cal_id)))
print("Print sorted student list:")
school.sort_s_l_gpa()
