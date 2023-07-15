import unittest
import util
import numpy as np


class TestUtilFunctions(unittest.TestCase):

    def setUp(self):
        util.load_saved_artifacts()

    def test_get_suburbs(self):
        suburbs = util.get_suburbs()
        self.assertIsNotNone(suburbs)
        self.assertIn("aberfeldie", suburbs)

    def test_get_types(self):
        types = util.get_types()
        self.assertIsNotNone(types)
        self.assertIn("house", types)
        self.assertIn("unit", types)

    def test_get_region_names(self):
        region_names = util.get_region_names()
        self.assertIsNotNone(region_names)
        self.assertIn("northern metropolitan", region_names)

    def test_predict_price(self):
        price = util.predict_price(4, 4, 5, 1, 200.0, 'aberfeldie', 'unit', 'northern metropolitan')
        print("Price:", price)
        print("Type:", type(price))
        self.assertIsNotNone(price)
        self.assertTrue(isinstance(price, float) or isinstance(price, np.float32))

if __name__ == '__main__':
    unittest.main()