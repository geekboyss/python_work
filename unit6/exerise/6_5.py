direct_rivel = {
        'nile': 'egypt',
        'huang': 'chine',
        'chang': 'japan',
        }

for key, value in direct_rivel.items():
    print("The" + key.title() + " runs through " + value.title())

print("------------")

for key in direct_rivel:
    print(key.title())

print("------------")

for value in direct_rivel.values():
    print(value.title())
