class CarComponents:
    def __init__(self, gastank: int, av_gasusage: int, key: bool, wheels: int, gas_pedal: bool, brake_pedal: bool):
        self.gastank = gastank
        self.av_gasusage = av_gasusage
        self.key = key
        self.wheels = wheels
        self.gas_pedal = gas_pedal
        self.brake_pedal = brake_pedal

    def __repr__(self):
        return f"Car components( gastank: {self.gastank} liters, average gas usage: {self.av_gasusae} lt/100 km, key turned: {self.key}, wheels: {self.wheels}"\
               f", gaspedal pressed: {self.gas_pedal}, brakepedal pressed: {self.brake_pedal})"

    def turn_key(self) -> bool:
        if self.key == True:
            self.key = False
            return self.key
        elif self.key == False:
            self.key = True
            return self.key

    def wheels_on(self) -> int:
        if self.wheels < 4:
            self.wheels = 4
        return self.wheels

    def fill_tank(self, amount) -> int:
        self.gastank += amount
        return self.gastank