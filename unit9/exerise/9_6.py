class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name : " + self.restaurant_name.title())
        print("type : " + self.cuisine_type.title())

    def open_restaurant(self):
        print("now we is open door")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def IceCreamStand(self):
        for fl in self.flavors:
            print(fl)


geek_restaurant = IceCreamStand('geek', 'dinner', 'hello', 'nihao')
geek_restaurant.IceCreamStand()




