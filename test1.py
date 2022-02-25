from io import BytesIO
from unittest import TestCase

import bigjson


JSON_FILE = b"""
{
     "Gender": "Male",
     "HeightCm": 175,
     "WeightKg": 75  
}
"""


class TestBasics(TestCase):

    def test_basics(self):
        file = BytesIO(JSON_FILE)
        data = bigjson.load(file)

        self.assertEqual(data['Gender'], 'Male')
        self.assertEqual(data['HeightCm'], 175)
        self.assertEqual(data['WeightKg'], 75)
        
if __name__ == '__main__':
     unittest.main(argv=['first-arg-is-ignored'], exit=False)