def show_magicians(magicians):
    print(magicians)

def make_great(magicians):
    n = len(magicians)
    new_magicians = []
    for i in range(0,n):
        temp = "The Great " + magicians[i]
        new_magicians.append(temp)
    return new_magicians

magicians = ['geek', 'alex', 'boy']

new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)



