print("Enter the number of student:")
n=int(input())
name_s=[None]*n
id_s=[None]*n
dob_s=[None]*n
print("Enter the number of course:")
m=int(input())
id_c=[None]*m
name_c=[None]*m

mark = [[None]*m for _ in range(n)]
def inputStudent(n):
    for i in range(n):
        id_s[i]=input("Enter id of student "+str(i+1)+ ":")
        name_s[i]=input("Enter name of student "+str(i+1)+ ":")
        dob_s[i]=input("Enter date of birth of student "+str(i+1)+ ":")

def inputCourse(m):
    for i in range(m):
        id_c[i]=input("Enter the id of course "+str(i+1)+ ":")
        name_c[i]=input("Enter the name of course "+str(i+1)+ ":")

#e is student id 
#k is course iddd
def addMark(e,k):
    for i in range(n):
        for j in range(m):
            if (id_s[i]==e and id_c[j]==k):
                mark[e][k]=input("Enter the mark:")
                
def checkStudent():
    for i in range(n):
        print("student "+str(i+1)+" id:" +str(id_s[i]))
        print("student "+str(i+1)+" name:" +str(name_s[i]))
        print("student "+str(i+1)+" date od birth:" +str(dob_s[i]))

def checkCourse():
    for i in range(m):
        print("course "+str(i+1)+" id:" +str(id_c[i]))
        print("course"+str(i+1)+" name:" +str(name_c[i]))

#a is id course
def checkMark(a):
    for i in range (m):
        if a==id_c[i] :
            for h in range(n):
                print("student "+str(h+1)+" id:" +str(id_s[h])+" ,mark:" +str(mark[h][i]))

    
inputStudent(n)
inputCourse(m)
while True:
    print("Do you want to add mark?(1 is yes/0 is no)")
    a=int(input())
    if a==1:
        aa=input("Enter the id of student you want to add mark:")
        bb=input("Enter the id of course:")
        addMark(aa,bb)
    else:
        break
b=int(input("Enter id course you want to check:")) 
checkMark(b)

