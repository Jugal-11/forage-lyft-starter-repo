import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn_data = [1,0.9,1,0.1]
        tire = OctoprimeTire(tire_worn_data)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_worn_data = [0.7,0.4,0.86,0.89]
        tire = OctoprimeTire(tire_worn_data)
        self.assertFalse(tire.needs_service())