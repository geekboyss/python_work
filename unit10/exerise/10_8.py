catname = 'cats.txt'
dogname = 'dogs.txt'

try:
    with open(catname) as fc:
        name1 = fc.read()

    with open(dogname) as fd:
        name2 = fd.read()

except FileNotFoundError:
    pass
else:
    print(name1)
    print(name2)
