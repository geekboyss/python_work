place = {}

active = True

while active:
    name = input("What is you name: ")
    address = input("where would you go?")

    place[name] = address

    repate = input("Do you have people")
    if repate == 'yes':
        continue
    else:
        active = False

    
for name, plac in place.items():
    print(name + " want to " + plac)

