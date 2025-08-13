def occurences(lst):
    freq={}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    max_ele=None
    max_cnt=0
    for key in freq:
        if freq[key]>max_cnt:
            max_cnt=freq[key]
            max_ele=key
    return max_ele,max_cnt
l=[]
for i in range(10):
    e=int(input("enter element"))
    l.append(e)
a,b=occurences(l)
print('the element with the maximum no of occurences is:',a)
print('the no of occurences is',b)