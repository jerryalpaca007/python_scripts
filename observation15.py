fl=open("SCHOOL.txt",'w')
fl.write("A school is an educational Institution designed to and learning provide learming spaces environments for the teaching of students under the direction of teachers.\n Most countries have systems of formal education, which is sometimes compulsory.\n In these systems, students progress through a series of schools.")
fl.close()
fr=open("SCHOOL.txt","r")
for i in range(3):
    info=fr.readline()
    print(info)
fr.close
frw=open("SCHOOL.txt","r+")
m=True
f2=open("MYSCHOOL.txt","w")
l=frw.readlines()
li=[]
ln=[]
for line in l:
    if "I" in line:
        li.append(line)
    else:
        ln.append(line)

f=open("SCHOOL.txt","w")
f.writelines(ln)
f.close()

f=open("MYSCHOOL.txt","w")
f.writelines(li)
f.close()

print()