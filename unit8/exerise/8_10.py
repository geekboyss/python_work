def show_magicians(magicians):
    print(magicians)

def make_great(magicians):
    n = len(magicians)

    for i in range(0,n):
        magicians[i] = "The Great " + magicians[i]



magicians = ['geek', 'alex', 'boy']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

