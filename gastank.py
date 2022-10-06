from gaspedal import GasPedal  # import from class Gaspedal

# ----- Global variables ------
tankContent = 10000

class Tank():
    def gastank (self):
        global gasUsed  # global variable that will be changed within the method

        gasPedal = GasPedal().gasPedal()  # Call the class Gaspedal and method gasPedal

        if gasPedal == True:  # If gaspedal = True so if it is pressed
            time = int(input('For how long did you drive?(in minuts): '))  # Ask how long the drive was
            gasUsed = time * 60  # Minuts * 60 seconds = total gas used
            return gasUsed  # Return gasUsed
        elif gasPedal == False:  # If gaspedal = False so if it is not pressed
            gasUsed = 0  # No gas is used
            print ('The gaspedal is not pressed and no gas is used.')
            return gasUsed  # Return gasUsed


    def gasoline(self):
        gasUsed = Tank().gastank() # Call the class Tank and method gastank

        if gasUsed > tankContent:  # If gasUsed is more than tankcontent
            print(f'The total amount of gas used is: {tankContent} units')
            print("There is no more gasoline left and the car has stopped moving\n")
            gasInTank = False  # Set gasIntank to False
            return gasInTank  # Return gasInTank
        else:
            print(f'The total amount of gas used is: {gasUsed} units')
            tankLeft = tankContent - gasUsed  # if not total tankcontent is used calculate rest
            print(f'There are {tankLeft} gas units left in the tank.\n')
            if tankLeft < 100:  # If there is less than 100 (safety limit) > advice to tank
                print('You are adviced the fill up the tank.\n')

            gasInTank = True  # Set gasIntank to True
            return gasInTank  # Return gasInTank


