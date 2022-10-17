import time
from car import Car
from engine import Engine
from car_components import CarComponents

engine = Engine(Engine.idNumber(), 270, 'Ferrari')
components = CarComponents(45, 8, False, 2, False, False)

car1 = Car(engine, components, 'Ferrari', Car.chassis_number(), 2022)

class Madlib:
    def play(self):
        self.start()  # Introduction method
        while True:  # While loop to check if the car is ready to start.
            self.wheels()  # Check wheels
            self.key()  # Check key
            if self.can_move():  # If car has 4 wheels and key is True > start
                print('Car is ready to go!')
                break
            elif self.can_move():
                print('Uho, car is not ready to go. Please check the wheels or the key.\n')  # If car does not have 4 wheels or key turned > retry
                continue
        # Car is running now
        self.left_in_tank()

    def can_move(self) -> bool:
        return Car.can_move(car1)

    def start(self) -> None:  # Introduction method
        print('----- The car is being assembled -----\n')  # Print
        # time.sleep(3)  # Effect
        print(f'This is the car:\n{car1}\n')  # Print the car
        while True:  # While statement for the input statement
            start = input('We need to check a few things before to start. Are you ready?(yes/no): ').lower()  # Ask if ready
            if start == 'yes':  # Go on
                break
            elif start == 'no':  # Quit
                print('Maybe next time')
                quit()
            else:  # Retry
                print('Please type yes or no.')
                continue

    def wheels(self) -> None:  # Check wheels method
        while True:  # While statement for the input statement
            wheels_on = input('Are all the 4 wheels on and firmly attached?(yes/no): ').lower()  # Input
            if wheels_on == 'yes':  # Go on
                print('Safety first.')
                break
            elif wheels_on == 'no':  # Wheels need to be attached
                print('Hold on wheels are being attached now.')
                # time.sleep(2)  # Effect
                components.wheels_on()  # Change wheels to 4
                print('Ready!')
                break
            else:  # Retry
                print('Please type yes or no.')
                continue

    def key(self) -> None:
        while True:  # While statement for the input statement
            key_on = input('Is the key turned on?(yes/no): ').lower()
            if key_on == 'yes':  # Go on
                print('Good to know')
                break
            elif key_on == 'no':  # Keys needs to be turned
                print('Turning key and starting car')
                components.turn_key()  # Turn key method from the components class
                break
            else:  # Retry
                print('Please type yes or no.')
                continue
# For every second the gas pedal is pressed then 1 unit of gas is burned from the tank
# For every 10 kilometers 1 liter of gas is used#
# The car can not move when there is no gasoline
# The car stops when the brake is pressed down and no gasoline is consumed
# The car can not move without its 4 wheels

    def gas_pedal_pressed(self):
        print(components.gas_pedal)
        print(components.av_gasusage)

        # Car is running

    def brake_pedal_pressed(self):
        print(components.brake_pedal)

    def gas_usage(self) -> int:  # Total gas used for trip
        self.distance = int(input('How many kilometers did you drive?: '))  # Input
        self.total_usage = self.distance // components.av_gasusage  # Usage in liters
        print(f'The trip cost {self.total_usage} liters.')  # Print statement
        return self.total_usage  # Return total usage

    def left_in_tank(self) -> int or float:  # This method will return an int or a float
        self.gas_usage()  # Call gas_usage method

        gas_left = components.gastank - self.total_usage  # gas left after trip
        if gas_left > 10:  # If there is more than 10 liters left
            print(f'The car has {gas_left} liters left in the tank.')  # print statement
        elif gas_left > 0 and gas_left <= 10:  # If there is between 1 and 10 liters left
            print(f'There are {gas_left} liters left. Please tank as soon as possible.')  # print statement
        elif gas_left <= 0:  # If there is no gas left
            # Another input and if statement to ask if you tanked during the trip?
            tank = input('Did you tank during the trip?(yes/no): ').lower()  # Ask if user filled tank
            if tank == 'yes':  # if yes
                self.amount = int(input('How many liters did you tank?: '))  # Ask how many liters

                # components.fill_tank(self.amount)
                gas_left_after_tanking = components.gastank  # To make the code work create variable gas_left_after_tanking that is equal to a filled tank

                gasamount_pre_tank = (gas_left_after_tanking * components.av_gasusage)  # Gas usage before tanking (so the whole tank to make it easy)
                rest_distance = self.distance - gasamount_pre_tank  # Calculate the rest distance that needs to be done
                gasamount_after_tank = gas_left_after_tanking - (rest_distance / components.av_gasusage)  # Calculate how much gas is used after tanking

                gas_left_after_tanking = components.gastank - gasamount_after_tank  # Amount of gas left after tanking and driving the rest of the kilometers
                components.gastank = gas_left_after_tanking  # set components.gastank equal to gas left after tank (so this variable is changed at the class level

                components.fill_tank(self.amount)  # Fil tank
                print(f'There is {components.gastank} liters left after the trip.')  # print statement
                return components.gastank  # return components.gastank

            elif tank == 'no':  # Not tanked
                max_kilometers = components.gastank * components.av_gasusage  # Calculate maximum amount of kilometers
                print(f'After {max_kilometers} kilometers the car stopped.')  # print statement

        components.gastank = gas_left  # Set componenets.gastank equal to gas_left
        return components.gastank  # return components.gastank



madlib = Madlib()


