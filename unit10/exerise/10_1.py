filename = 'learning_python.txt'

with open(filename) as file_object:
    #content = file_object.read()
    lines = file_object.readlines()

#print(content.rstrip())

for line in lines:
    print(line.rstrip())

