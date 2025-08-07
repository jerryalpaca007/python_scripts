list_user=["user1","user2","user3","user4","user5","user6","user7","user8","user9","user10"]
list_password=['password1','password2','password3','password4','password5','password6','password7','password8','password9','password10']
lu=len(list_user)
lp=len(list_password)
username=input('enter username:')
password=input('enter password:')
for i in range(lu):
    if list_user[i]==username:
        print(i)
for j in range(lp):
    if list_password[j]==password:
        print(j)