import random

class Brake:
    def brakes(self):
        # Make simple automatic choice of yes or no for the boolean
        choicelst = ['yes', 'no']
        randnum = random.randint(0,1)
        yesno = choicelst[randnum]
        print(yesno)

        # Let boolean decide if the car is breaking or not
        if yesno == 'yes':
            gasUsage = 0
            print (f'Your gas usages is {gasUsage} unit per second')
        elif yesno == 'no':
            gasUsage = 1
            print (f'Your gas usages is {gasUsage} unit per second')
        else:
            print ('Not a valid choice')


Brake().brakes()