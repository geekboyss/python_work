class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0    

    def describe_restaurant(self):
        print("name : " + self.restaurant_name.title())
        print("type : " + self.cuisine_type.title())

    def open_restaurant(self):
        print("now we is open door")
    
    def increment_number_served(self, num):
        self.number_served += num


geek_restaurant = Restaurant('geek', 'dinner')
geek_restaurant.describe_restaurant()

print("All have " + str(geek_restaurant.number_served))
geek_restaurant.number_served = 10
print("All have " + str(geek_restaurant.number_served))
geek_restaurant.increment_number_served(100)
print("All have " + str(geek_restaurant.number_served))

