def describe_pet(pet_name, animal_type = 'dog'):
    """ display pet information """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('willie')

describe_pet(pet_name = 'harry', animal_type = 'hamster')



