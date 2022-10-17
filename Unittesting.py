import unittest

from car import Car
from engine import Engine
from car_components import CarComponents

engine1 = Engine(Engine.idNumber(), 270, 'Ferrari')
components1 = CarComponents(45, 8, True, 2, False, False)
car1 = Car(engine1, components1, 'Ferrari', Car.chassis_number(), 2022)


class TestCar(unittest.TestCase):
    def test_can_move(self):
        test_car = car1
        actual = test_car.can_move()
        self.assertTrue(actual)


class TestCarComponents(unittest.TestCase):
    def test_wheels_on(self):
        test_component = components1
        actual = test_component.wheels_on()
        self.assertEqual(actual, 2)

class testEngine(unittest.TestCase):
    pass

TestCar().test_can_move()
# TestCarComponents().test_wheels_on()
#
# if __name__ == 'main':
#     unittest.main()