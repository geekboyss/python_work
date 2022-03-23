sandwich_orders = ['pastrami', 'geek', 'tuna', 'alxe']

finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you " + sandwich + " sandwich")
    finished_sandwich.append(sandwich)

print(finished_sandwich)

