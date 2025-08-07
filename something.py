x=int(input('enter a number'))
s=0
u=1
if u>0:
    u=u+1
    for i in range(1, x):
        if(x % i == 0):
            s= s + i
    if (s==x):
        print('Number is a Perfect Number')
    else:
        print('Number is not a Perfect Number')
while u > 1:
    u=input('continue')
    if u == 'yes':
        print('ok')
        
