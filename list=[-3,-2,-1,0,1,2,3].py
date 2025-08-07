list=[-3,-2,-1,0,1,2,3]
positive=[]
negative=[]
for i in range(len(list)):
    if list[i]>0:
        positive.append(list[i])
    if list[i]<0:
        negative.append(list[i])
print('negative numbers:',negative)
print('positive numbers',positive)
print('main list',list)