class Wheels:
    def wheelsOnCar(self):
        wheelsOn = input('Are all 4 wheels attached to the car?(yes/no): ').lower()

        if wheelsOn == 'yes':
            wheelsOn = True
            return wheelsOn
        elif wheelsOn == 'no':
            wheelsOn = False
            return wheelsOn
        else:
            return('Please make a choice between yes or no.')
