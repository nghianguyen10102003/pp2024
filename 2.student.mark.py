class course:
    def __init__(self):
        self.__id=0
        self.__name=0
    def set(self,id,name):
        self.__id=id
        self.__name=name
    def get(self):
        return f"Id course:{self.__id},Name course:{self.__name}"
class student(course):
    def __init__(self):
        super().__init__()
        self.__dob=0
    def set(self,id,name,dob):
        super().set(id,name)
        self.__dob=dob
    def get(self):
        return  f"Id student:{self.__id},Name studnet:{self.__name},Date of Birth:{self.__dob}"
students = []
courses = []
s=student()
number_s=int(input("Enter number of student:"))
for i in range(number_s):
    s=student()
    id=input("Enter the id of student "+str(i+1)+":")
    name=input("Enter the name of student " +str(i+1)+":")
    dob=input("Enter the date of birth of student"+str(i+1)+":")
    s.set(id,name,dob)
    students.append(s)
number_c=int(input("Enter the number of course:"))
for i in range(number_c):
    c=course()
    id=input("Enter the id of course "+str(i+1)+":")
    name=input("Enter the name of course " +str(i+1)+":")
    c.set(id,name)
    courses.append(c)
print("you want to show the list of student ? (1 is yes/0 is no)")
chose=int(input())
if chose ==1:
    for s in students:
        print(s.get())
else:
    pass
print("you want to show the list of course ? (1 is yes/0 is no)")
chosee=int(input())
if chosee ==1:
    for c in courses:
        print(c.get())
else:
    pass


