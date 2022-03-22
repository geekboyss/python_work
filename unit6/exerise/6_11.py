cities = {
        'shanghai':{
            'country':'china',
            'population': 1234,
            'fact': 'beautiful',
            },
        'tokoy':{
            'country': 'japan',
            'population': 34,
            'fact' : 'normal',
            },
        'newyok':{
             'country': 'amercian',
             'population': 43434,
             'fact': 'money',
            }
        }

for name , cititys in cities.items():
    print("name : " + name)
    for key ,value in cititys.items():
        if key == 'population' :
            print(key + ":" + str(value))
        else:
            print(key + ":" + value)


