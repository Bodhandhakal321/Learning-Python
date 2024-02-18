class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)  
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())
# print(my_tesla.full_name())

safari = Car("Tata", "SAFARI")
safariThree = Car("Tata", "Nexon")
print(safari.fuel_type())

print(Car.total_car)



# my_car = Car("Toyota", "HILUX")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)


# questions
# __init__ is a constructor 
# addinng method to a class and displays the full name of class
# inheritance creating electriccar class that inherits from the car class and has an additional attribute battery_size
# __ means making private
# encapsulation modifying car class the brand attribute to private 
# setter for us
#  learning polymorphism by defining a method fuel_type in both car and electiccar 
# class variable adding a class varibale which keeps track of the no of car created