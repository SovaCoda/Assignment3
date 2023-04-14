import unittest
from bmi import convertWeight, convertHeight, doMath, calculateBMI, classify

class TestMyModule(unittest.TestCase):

    def test_convertWeight(self):
        self.assertEqual(convertWeight(100), 45)

    def test_convertHeight(self):
        self.assertEqual(convertHeight(100), 2.5)

    def test_doMath(self):
        self.assertEqual(doMath(45, 2.5), 7.2)

    def test_calculateBMI(self):
        self.assertEqual(calculateBMI(100, 100), 7.2)

    def test_classify(self):
        self.assertEqual(classify(18.4), "Underweight")
        self.assertEqual(classify(18.5), "Normal Weight")
        self.assertEqual(classify(20), "Normal Weight")
        self.assertEqual(classify(24.9), "Normal Weight")
        self.assertEqual(classify(25), "Overweight")
        self.assertEqual(classify(26), "Overweight")
        self.assertEqual(classify(29.9), "Overweight")
        self.assertEqual(classify(30), "Obese")