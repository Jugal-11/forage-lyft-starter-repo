import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn_data = [0,0.9,1,0]
        tire = CarriganTire(tire_worn_data)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_worn_data = [0.7,0.4,0.66,0.89]
        tire = CarriganTire(tire_worn_data)
        self.assertFalse(tire.needs_service())