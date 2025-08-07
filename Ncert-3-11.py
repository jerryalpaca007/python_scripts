#
#
#
import math
#n=int(input('enter no of values: '))
#x=[]
j=0
#for i in range(n):
#xv=int(input('enter x value: '))
    #x.append(xv)
x=eval(input('enter a list of values: '))
n=len(x)
#print('the list of integers ',x)
sor=sorted(x)
print('the sorted list is ',sor)
for i in range(len(x)):
    j=j+x[i]
print(j)

if n%2 != 0:
    print('odd no of observations')
    m='odd'
elif n%2 == 0:
    print('even no of observations')
    m='even'

# if m=='even':
e_med=(n+1)/2
u=math.ceil(e_med)
print('actual median ',e_med)
print('median is',math.ceil(e_med))
print('median term is ',x[u-1])
#odd_median=(n/2+(n+1)/2)/2

#u=((n+1)/2)
