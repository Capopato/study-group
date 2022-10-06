import random  # Import random

class Engine():  # class Engine
    def engineNumber(self):
        idnum = ''  # Empty string

        for i in range(0, 10):  # Set range
            r = random.randrange(0, 9)  # Generate engine number
            idnum += idnum.join(str(r))  # Add engine number to empty string
        # Return engine number
        return(idnum)

    def engineBrand(self):
        # Just a selection of brand options
        engineBrandOptions = ['Ferrari', 'Lamborghini', 'Koeningseggs', 'Volkswagen', 'Opel', 'Renault', 'Audi', 'BWM',
                        'Mercedes']

        # Generate a random number with lengt of list -1 to prevent index out of range error.
        r = random.randint(0, len(engineBrandOptions) - 1)
        engineBrand = engineBrandOptions[r]  # Pick random engine brand from engineBrandOptions
        # Return engineBrand
        return (engineBrand)