# Eric Sengvanhpheng
# July 11, 2026
# Advanced Python Module 7.2

import unittest
from city_functions import get_formatted_name

# create a test class that inherits unittest testing methods from unittest.TestCase
class CitiesTestCase(unittest.TestCase):

    # create function for testing
    def test_city_country(self):

        # run function using these inputs 
        result = get_formatted_name('santiago', 'chile')
        # expect results to match this value
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

