pizzas = ['geek', 'boy', 'girl']
friend_pizzas = pizzas[:]

pizzas.append('dog')
friend_pizzas.append('cat')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)




