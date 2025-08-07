l=int(input('enter no of values'))
ls=[]
for i in range(l):
    x=int(input('enter a no'))
    ls.append(x)
L=len(ls)
s=ss=ls[0]
for i in range(1,L):
    if ls[i]>s:
        ss=s
        s=ls[i]
    elif ls[i]>ss:
        ss=ls[i]
print(ss)