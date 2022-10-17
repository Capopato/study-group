import random
from turtledemo import paint
from engine import Engine
from car_components import CarComponents
# from gastank import Gastank

# Car file. Create class Car

# This car has an engine, a gas tank, a key, four wheels, a brake and gas pedals.
#
# The car can only move if the key is turned on
# For every second the gas pedal is pressed then 1 unit of gas is burned from the tank
# The car can not move when there is no gasoline
# The car stops when the brake is pressed down and no gasoline is consumed
# The car can not move without its 4 wheels

# This car also has

# a brand
# a chassis number
# a production year

# The engine has

# an identification number
# a brand

class Car:
    def __init__(self, engine: Engine, gastank: int, key: bool, wheels: int, gas_pedal: bool, brake_pedal: bool, brand: str,
                 chassis_number: int, production_year: int):
        self.engine = engine
        self.gastank = gastank
        self.key = key
        self.wheels = wheels
        self.gas_pedal = gas_pedal
        self.brake_pedal = brake_pedal
        self.brand = brand
        self.chassis_number = chassis_number
        self.production_year = production_year
        self.horsepower = []

    def __repr__(self):
        return f"Car ({self.engine}, gastank: {self.gastank} liters, key turned: {self.key}, wheels: {self.wheels}"\
               f", gaspedal pressed: {self.gas_pedal}, brakepedal pressed: {self.brake_pedal}, brand: {self.brand}, " \
               f"chassis number: {self.chassis_number}, production year: {self.production_year}"

    def can_move(self):
        return self.key and self.gastank > 0

    def turn_key(self):
        if self.key == True:
            self.key = False
        elif self.key == False:
            self.key = True

    def add_horsepower(self, horsepower: Engine):
        self.horsepower.append(horsepower.horsepower)

    def total_horsepower(self) -> int:
        total_horsepower = sum(self.horsepower)
        return total_horsepower

    @classmethod # TODO: What does this classmethod do and why does it work? If I remove it I can the follow error: Car.chassis_number() missing 1 required positional argument: 'self'
    def chassis_number(self) -> int:
        chas_num = '' # Empty string for engine id number

        for i in range(0, 8):  # Set range for 13 characters
            r = random.randrange(0,9)  # Generate numbers between 0-9
            chas_num += chas_num.join(str(r))  # Append generated numbers to empty string

        return(int(chas_num))  # Return chassis number


engine1 = Engine(Engine.idNumber(), 270, 'Ferrari')
engine2 = Engine(Engine.idNumber(), 255, 'Mercedes')
car1 = Car(engine1, 100, False, 4, True, False, 'Ferrari', Car.chassis_number(), 2022)
car2 = Car(engine2, 100, False, 4, True, False, 'Mercedes', Car.chassis_number(), 2020)

car1.add_horsepower(engine1)
car1.add_horsepower(engine2)


print(car1.chassis_number)