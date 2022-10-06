import random

from brake import Brake
from wheels import Wheels
from gastank import Tank
from key import Key
from engine import Engine

# ----- Global variables ------
# These global variables are a pre set and may or may not be changed in the different methods.
carIsDriving = True
gasPedal = False
keyturned = False
gasInTank = True
gasUsed = 0
brake = False


class Car():
    def carDriving(self):
        while carIsDriving:  # While carIsDriving = True
            keyTurned = Key().key()  # Asks if the key is turned on. If not > break
            wheels = Wheels().wheelsOnCar()  # Ask is the wheels are attached. If not > break
            if keyTurned == True:

                if wheels == True:
                    print('Key is turned on and the car has started\n')  # print statement
                    Tank().gasoline()  # Imports class Tank and def gasoline.
                    Brake().brakes()  # Imports class Brake and def brakes.
                    break
                else:
                    print('The car does not have all 4 wheels and cannot drive.')  # Print statement if wheels = False
                    break  # Break while loop

            else:
                print('The carkey is not turned on so the car cannot drive.')  # Print statement if keyTurned = False
                break  # Break while loop


    def brandCar(self):
        # Just a selection of brand options
        brandOptions = ['Ferrari', 'Lamborghini', 'Koeningseggs', 'Volkswagen', 'Opel', 'Renault', 'Audi', 'BWM',
                        'Mercedes']

        # Generate a random number with lengt of list -1 to prevent index out of range error.
        r = random.randint(0, len(brandOptions)-1)
        carBrand = brandOptions[r]  # Pick a random brand.
        # Return carBrand
        return (carBrand)


    def chassisNumber(self):
        chassNum = ''  # Empty string

        for i in range(0, 10):  # Select a range for len of chassnum
            r = random.randrange(0, 9)  # Random range with lenght of chassnum
            chassNum += chassNum.join(str(r))  # Empty string is filled with random range
        # Return chassNum
        return (chassNum)


    def productionYear(self):
        prodYearCar = ''  # Empty string

        # Generate a random number between year 2000 and tear 2022.
        r = random.randint(2000, 2022)
        prodYearCar = prodYearCar.join(str(r))  # Add the generated year to the empty string
        # Return prodYearCar
        return(prodYearCar)




