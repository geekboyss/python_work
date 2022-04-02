#from car import Car, ElectricCar
#
#my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#
#my_tesla = ElectricCar('tesla', 'roadster', 2019)
#print(my_tesla.get_descriptive_name())

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()


# 9.4.4
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


# 9.4.5 导入所有类
# form car import *
