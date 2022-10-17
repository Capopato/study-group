import random

# The engine has

# an identification number
# a brand

class Engine:
    brandOptions = {'Ferrari': 750,
                         'Honda': 125,
                         'Toyota': 175,
                         'Mercedes-Benz': 310,
                         'Volvo': 210,
                         'Jaguar': 215,
                         'Audi': 255,
                         'BMW': 270}

    def __init__(self, id_number: int, horsepower: int, brand: str):
        self.id_number = id_number
        self.horsepower = horsepower
        self.brand = brand

    def __repr__ (self):
        return f"Engine( ID_number: {self.id_number}, Brand: {self.brand})"

    @classmethod
    def idNumber(cls) -> int:
        idnum = '' # Empty string for engine id number

        for i in range(0, 8):  # Set range for 13 characters
            r = random.randrange(0,9)  # Generate numbers between 0-9
            idnum += idnum.join(str(r))  # Append generated numbers to empty string

        return(int(idnum))  # Return idNum