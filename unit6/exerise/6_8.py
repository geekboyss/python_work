huahua = {
        'type': 'dog',
        'host': 'geek',
        }

liangliang = {
        'type': 'cat',
        'host': 'alex',
        }

pets = [huahua, liangliang]

for pet in pets:
    print("type " + pet['type'] + ",host " + pet['host'])
    
