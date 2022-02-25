from unittest import TestCase

BMI_Range={0:[0,18.4],1:[18.5,24.9],2:[25,29.9],3:[30,34.9],4:[35,39.9],5:[40,100]}
Health_Risk=["Malnutrition risk","Low risk","Enhanced risk","Medium risk","High risk","Very high risk"]
BMI_Category=["Underweight","Normal weight","Overweight","Moderately obese","Severely obese","Very severely obese"]
BMI=round(60/(186/100)**2,2)    
class TestBasics(TestCase):

    def test_basics(self):
        self.assertNotEqual(BMI, 4)
        self.assertEqual(BMI_Range[0], [0,18.4])
        self.assertNotEqual(BMI_Range[5], [0,18.4])
        self.assertEqual(len(Health_Risk), 6)
        self.assertEqual(len(BMI_Category), 6)
if __name__ == '__main__':
     unittest.main(argv=['first-arg-is-ignored'], exit=False)