# Max Jankowski
# CSD-325 Module 7 Assignemnt
# Bellevue University


import unittest
from city_functions import city_country

# tests for the city_country function created earlier
class TestCityCountry(unittest.TestCase):

    def test_city_country(self): # test to see if city and country names work 

        result = city_country("santiago", "chile")
        self.assertEqual(result, "santiago, chile")


if __name__ == '__main__':
    unittest.main()