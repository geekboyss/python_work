filename = 'guest_book.txt'


 
while True:
    name = input('Plase enter name :')
    if name == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')

