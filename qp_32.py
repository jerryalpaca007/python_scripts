xs=input('enter a list of alphabets seprated by a comma: ')
xr=xs.split(sep=',')
x=list(xr)
upper=[]
lower=[]
for i in range(len(x)):
    if str(x[i]).isupper():
        upper.append(x[i])
    elif str(x[i]).islower():
        lower.append(x[i])
print('upper case letters list ',upper)
print('lower case letters list ',lower)
