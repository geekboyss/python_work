userlist = ['admin', 'Eric', 'Geek', 'Alex']

for user in userlist:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ",thank you for logging in ageain")


if userlist:
    print("We have users")
else:
    print("We need to find some users!")

print("delete " + userlist.pop())
print("delete " + userlist.pop())
print("delete " + userlist.pop())
print("delete " + userlist.pop())


if userlist:
    print("We have users")
else:
    print("We need to find some users!")
