def make_car(made, model, **more):
    new_car = {}

    new_car['made'] = made
    new_car['model'] = model
    
    for key, value in more.items():
        new_car[key] = value
    
    return new_car

car = make_car('subaru', 'outback',
               color='green',
               tow_package=True)
for key, value in car.items():
    print(key + " :" + str(value))


