fyl=open("SCHOOL.txt",'w')
fyl.write("A school is an educational Institution designed to and learning provide learming spaces environments for the teaching of students under the direction of teachers.\n Most countries have systems of formal education, which is sometimes compulsory.\n In these systems, students progress through a series of schools.")
fyl.close()
fylr=open("SCHOOL.txt","r")
for i in range(3):
    info=fylr.readline()
    print(info)
fylr.close
fylrw=open("SCHOOL.txt","r+")
m=True
fyl2=open("MYSCHOOL.txt","w")
while m==True:
    m=fylrw.readline()
    print(m)
    for i in range(len(m)):
        if m[i] == 'I':
            fyl2.write(m)