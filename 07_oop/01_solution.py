class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)  
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    


# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())
# print(my_tesla.full_name())

# safari = Car("Tata", "SAFARI")
# safari.model = "city"


# safariThree = Car("Tata", "Nexon")
# print(safari.model)

# print(Car.total_car)

# print(safari.general_desc())
# print(Car.general_desc())



# my_car = Car("Toyota", "HILUX")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
    
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model X")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())


# questions
# __init__ is a constructor 
# addinng method to a class and displays the full name of class
# inheritance creating electriccar class that inherits from the car class and has an additional attribute battery_size
# __ means making private
# encapsulation modifying car class the brand attribute to private 
# setter for us
#  learning polymorphism by defining a method fuel_type in both car and electiccar 
# class variable adding a class varibale which keeps track of the no of car created
# adding a static method to the Car class that returns the description of car
# @staticmethod is a decoraters
# using property decorators in the Car class to make the model attribute read only leaned @proprty decorators
# use of isinstance() to check my_tesla is an instance of Car and ElectricCar
#  multiple inheritance create two class battery and engine let ElectricCar inherit from both