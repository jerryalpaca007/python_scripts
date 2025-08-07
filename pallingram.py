      
user_acc = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}

print(user_acc)
username=input("Enter your username: ")
password = input("Enter your password: ")
'''if username not in user_accounts:
    print("You are not a valid user of the system.")
else:'''
if user_acc[username] == password:
    print("You are now logged into the system.")
    '''else:
        print("The password is invalid.")'''
print(user_acc[username].index)