x=int(input('enter a number from 0-9999'))
thousand=x//1000
print(thousand)
hundred=(x%1000)//100
print(hundred)
ten=(x%100)//10
print(ten)
one=(x%10)
print(one)
conv={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
if thousand==0 and hundred==0 and ten==0:
    v4=conv[one]
    print(v4)
elif thousand==0 and hundred==0:
    v3=conv[ten]
    v4=conv[one]
    print(v3,v4)
elif thousand==0:
    v2=conv[hundred]
    v3=conv[ten]
    v4=conv[one]
    print(v2,v3,v4)
else:
    v1=conv[thousand]
    v2=conv[hundred]
    v3=conv[ten]
    v4=conv[one]
    print(v1,v2,v3,v4)
