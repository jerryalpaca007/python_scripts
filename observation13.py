print('Extracting Values From a user Given Key Using Functions')
print('-------------------------------------------------------\n')
def extval(d_list, key):
    e_val = []
    for d in d_list:
        if key in d:
            e_val.append(d[key])
    return e_val
d_list=[]
print("Input Data")
print("----------\n")
n=int(input('enter no of records'))
for i in range(n):
    print('\nrecord no:',i+1)
    print('-----------------\n')
    key1 = input("Enter first key: ")
    value1 = input("Enter first value: ")
    print()
    key2 = input("Enter second key: ")
    value2 = input("Enter second value: ")
    tdict = {key1: value1, key2: value2}
    d_list.append(tdict)
print('\nOutput Data')
print('-----------\n')
exkey=input('enter the name of the key to extract:')
names=extval(d_list,exkey)
print('The extracted values from the given key is:',names)


