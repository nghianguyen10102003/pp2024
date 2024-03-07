print("Enter the number of student:")
n=int(input())
name_s=[None]*n
id_s=[None]*n
dob_s=[None]*n
print("Enter the number of course:")
m=int(input())
id_c=[None]*m
name_c=[None]*m

mark=[None][None]*n*m
def inputStudent(n):
    for i in range(n):
        id_s[i]=input("Enter id of student "+str(i+1)+ ":")
        name_s[i]=input("Enter name of student "+str(i+1)+ ":")
        dob_s[i]=input("Enter date of birth of student "+str(i+1)+ ":")

def inputCourse(m):
    for i in range(m):
        id_c[i]=input("Enter the id of course "+str(i+1)+ ":")
        name_c[i]=input("Enter the name of course "+str(i+1)+ ":")

#e la id hoc sinh
#k la id mon hoc
def addMark(e,k):
    for i in range(n):
        for j in range(m):
            if (id_s[i]==e and id_c[j]==k):
                mark[i][j]=input("Enter the mark:")
                
            else:
            
    


inputStudent(n)
inputCourse(m)
while True:
    print("Do you want to add mark?(1 is yes/0 is no)")
    a=input()
    if int(a)==1:
        aa=input("Enter the id of student you want to add mark:")
        bb=input("Enter the id of course:")
        addMark(aa,bb)
    else:
        break



    
        

