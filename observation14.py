fyl=open('School.txt','w+')
fyl.write('A school is an Educational institution designed to provide learning spacesand learning environments for the teaching of students under the directionof teachers.')
fyl.close()

fol=open('School.txt','r')
vcnt=0
ccnt=0
ucnt=0
lcnt=0
m=" "
while m:
    m=fol.readline()
    for i in range(len(m)-1):
        if m[i] in ['A','a','E','e','I','i','O','o','U','u']:
            vcnt+=1
        elif m[i] in [' ','?',',','.']:
            continue
        if m[i].isupper():
            ucnt+=1
        elif m[i].islower():
            lcnt+=1
        else:
            ccnt+=1

print('No of vowels in the line is :',vcnt)
print('No of consonants in the line is :',ccnt)
print('No of uppercase characters is :',ucnt)
print('No of lowercase characters is :',lcnt)

