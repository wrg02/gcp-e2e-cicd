import unittest

target = __import__("app")

class TestPopulation(unittest.TestCase):
    def test_census_data(self):
        """
        Test that method returns expected text
        """
        lat = "47.6062"
        long = "-122.3321"
        county, population, density = target.get_census_data(lat, long)
        self.assertEqual(population, 2252782)
    
if __name__ == '__main__':
    unittest.main()