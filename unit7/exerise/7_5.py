prompt = "Please enter age: "

while True:    
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("free")
    elif age < 12:
        print("10$")
    else:
        print("15$")


