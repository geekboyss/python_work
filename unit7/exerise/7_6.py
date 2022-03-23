prompt = "Please enter age: "

#age = input(prompt)
#age = int(age)
#
#while age > 0:    
#    if age < 3:
#        print("free")
#    elif age < 12:
#        print("10$")
#    else:
#        print("15$")
#
#    age = input(prompt)
#    age = int(age)

# 7-7-2

#active = True
#while active:
#    age = input(prompt)
#    if age == 'quit':
#        active = False
#        continue
#    else:
#        age = int(age)
#    
#    if age < 3:
#        print("Free")
#    elif age < 12:
#        print("10$")
#    else:
#        print("15$")

# 7-7-3

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)

    if age < 3:
        print("Free")
    elif age < 12:
        print("10$")
    else:
        print("15$")
