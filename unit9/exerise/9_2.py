class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name : " + self.restaurant_name.title())
        print("type : " + self.cuisine_type.title())

    def open_restaurant(self):
        print("now we is open door")


geek_restaurant = Restaurant('geek', 'dinner')
geek_restaurant.describe_restaurant()

boy_restaurant = Restaurant('boy', 'lunch')
boy_restaurant.describe_restaurant()


