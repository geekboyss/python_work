filename = 'learning_python.txt'

with open(filename) as file_object:
    content = file_object.read()
    #lines = file_object.readlines()
ret = content.replace('Python', 'C')

print(ret.rstrip())

#for line in lines:
#    ret = line.replace('Python', 'C')
#    print(ret.rstrip())

