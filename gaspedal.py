class GasPedal:
    def gasPedal (self):
        pedalPressed = input('Is the gaspedal pressed?(yes/no): ').lower()  # Ask input

        print(' ') # Print empty space (for better layout)

        if pedalPressed == 'yes':  # Pedal is pressed
            gasPedal = True  # Set gas pedal to True
            return gasPedal  # Return gas pedal
        elif pedalPressed == 'no':  # Pedal is not pressed
            gasPedal = False  # Set gas pedal to False
            return gasPedal  # Return gas pedal
        else:
            return('Please make a choice between yes or no.')  # Let user make a valid choice
