import time

class Carr(object):
    # TODO: Question: How would I hand the code below to let it run.
    #  I get the following error: TypeError: Car.__init__() missing 8 required positional arguments: 'brand', 'chassisNumber', 'productionYear', 'engine', 'gastank', 'key', 'gasPedal', and 'breakPedal'#
    # def __init__(self, brand, chassisNumber, productionYear, engine, gastank, key, gasPedal, breakPedal):
        #     self.brand = 'Ferrari'
        #     self.chassicNumber = '123456'
        #     self.productionYear = '2022'
        #     self.gastank = '848'
        #     self.engine = '450'
        #     self.key = 'on'
        #     self.gasPedal = 'stiff'
        #     self.breakPedal = 'stiff'

    def __init__ (self):
        # I thought it would be nice to ask for input about the car.
        # self.brand = input('Brand: ')
        # self.chassicNumber = int(input('Chassis number: '))
        # self.productionYear = input('Production year: ')
        # self.engine = int(input('Engine (how many HP): '))
        # self.gastank = int(input('Engine (how many gas units): '))
        # self.key = input('Key (on or off): ').lower()
        # self.gasPedal = input('Gaspedal (stiff or loose): ')
        self.gas_usage = None
        self.breakPedal = input('Breakpedal (stiff or loose): ')

    # TODO: Make if statement for the def turn_on. If answer is 'on' then > other functiuons. Else: pass
    def turn_on(self):
        if self.key == 'on':
            print('\nCar is running and ready to start your trip. \n')
        else:
            print("Please insert key and try again.\n")
            quit()

    def gas(self):
        self.gas_usage = 1

        print('You have driving a long drive and are curious about your total gas usage.\n')
        # When gaspedal is pressed the car consumes 1 unit of gas per second
        time_drive = input('For how long did you drive? (in hours): ')

        # If gas_uage was another metric than 1 I would need to make another calculation
        total_gas_usage = int(time_drive) * 60
        minimum_gas = 50
        total_gas = self.gastank - total_gas_usage
        print(f'\nTotal gas used is: {total_gas_usage}\n')

        if total_gas < minimum_gas:
            tank_possible = input(f'You have reached the minimum gas of {minimum_gas}. Is there a gasstation nearby? (yes/no): \n').lower()
            if tank_possible == 'yes':
                gas_usage_before_tanking = total_gas_usage - (total_gas_usage - (self.gastank - minimum_gas))
                gas_usage_after_tanking = total_gas_usage - gas_usage_before_tanking
                to_tank = self.gastank - minimum_gas
                print(f'Before tanking you had: {self.gastank-gas_usage_before_tanking} gasunits left')
                print(f'You tanked: {to_tank} gasunits')
                print(f'After tanking you had a full tank with: {self.gastank} gasunits')
                print(f'After driving the whole trip there is {self.gastank - gas_usage_after_tanking} gas left in the tank')
            if tank_possible == 'no':
                print(f'After user {self.gastank} units of gas you have run out and the car stopped moving')
        else:
            print(f'Total gas left in the tank is: {total_gas}')
            if total_gas < minimum_gas:
                print('Gas running low. Please tank')

    def breaks(self):
        speed = int(input('How fast are u driving?(in km/s): '))
        breaking = input("Are you breaking?(yes/no): ").lower()
        if breaking == 'yes':
            self.gas_usage = 0
            print(f'Your gas usage is {self.gas_usage} unit')
            breakDistance = ((speed / 10) ** 2) / 2
            print(f'Your break distance at the speed of {speed} km/h is {int(breakDistance)} meters. Please take caution.')
        elif breaking == 'no':
            self.gas_usage = 1
            print(f'Your gas usage is {self.gas_usage} unit')
        else:
            print('Please choose between yes or no.')

    def wheels(self):
        all4wheels = input('Are all four wheels attached to the car?(yes/no) : ').lower()
        if all4wheels == 'yes':
            pass
        elif all4wheels == 'no':
            pass
        else:
            print('Please choose between yes or no.')


car1 = Car()
# car1.turn_on()
# car1.gas()
car1.breaks()
# car1.gas()




    # TODO: Optional do activate all from this method
    # def kata(self):
    #     self.turn_on()
    #     self.gas_usage()