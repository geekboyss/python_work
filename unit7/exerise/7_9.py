sandwich_orders = ['pastrami', 'geek','pastrami', 'tuna', 'alxe', 'pastrami']

finished_sandwich = []

print("pastrami = 0")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you " + sandwich + " sandwich")
    finished_sandwich.append(sandwich)

print(finished_sandwich)

