
import unittest
import NameGenerator

class NameGeneratorTestCases(unittest.TestCase):

    #A valid string test
    def test1(self):
        result = NameGenerator.name("Piers", "Borngasser")
        self.assertEqual(result, "Piers Borngasser")

    #An invalid int value for x
    def test2(self):
        result = NameGenerator.name(3,"Borngasser")
        #print(result)
        self.assertEqual(result, "Need two strings for a name")

    #A very not normal name but a valid one
    def test3(self):
        result = NameGenerator.name("3.14ers", "Borngasser")
        #print(result)
        self.assertEqual(result, "3.14ers Borngasser")


if __name__ == "__main__":
    unittest.main()
