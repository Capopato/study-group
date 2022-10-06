class Brake:
    def brakes(self):
        global brake  # Global variable

        braking = input('Did you brake during your trip?(yes/no): ').lower()  # Ask if user has brakes during trip

        if braking == 'yes':  # If braked
            speed = int(input('How fast were u driving?(in km/s): '))  # Ask input
            conditions = input('Were the conditions normal or wet?(normal/wet): ')  # Ask input

            if conditions == 'normal':  # Calculate for normal conditions
                brakeDistance = ((speed / 10)**2)  # Formula braking distance
                print(f'The brakedistance under normal conditions at the speed of {speed} km/h is {int(brakeDistance)} meters. Please be aware and take caution.')  # Print speed and braking distance
                brake = True  # Return brake is True
                return brake  # Return brake
            elif conditions == 'wet':  # Calculate for wet conditions
                brakeDistance = ((speed/10)**2) + (((speed/10)**2)/2)  # Formula braking distance
                print(f'The brakedistance under normal conditions at the speed of {speed} km/h is {int(brakeDistance)} meters. Please be aware and take caution.')  # Print speed and braking distance
                brake = True  # Return brake is True
                return brake  # Return brake

        elif braking == 'no':  # If there was no braking
            brake = False  # Brake is False
            return brake  # Return brake
        else:
            print('Please make a choice between on or off')  # Let user make a valid choice