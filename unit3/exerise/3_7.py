namelist = ['geek', 'alex', 'girl']

print("I will invite " + str(namelist))

print("now i can invite more people")

namelist.insert(0, 'xiaobai')
namelist.insert(2, 'xiaoming')
namelist.append('xiaohei')


print("I will invite " + str(namelist))

print("I am sorry for my desk")

name = namelist.pop()
print("I can't invite " + name)
name = namelist.pop()
print("I can't invite " + name)
name = namelist.pop()
print("I can't invite " + name)
name = namelist.pop()
print("I can't invite " + name)

print("I will invite " + str(namelist))
namelist.pop()
namelist.pop()
print("namelist = " + str(namelist))

