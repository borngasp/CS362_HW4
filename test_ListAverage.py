import unittest
import ListAverage

class ListAverageTestCases(unittest.TestCase):

    #A valid list to test
    def test1(self):
        result = ListAverage.average([2,4,6])
        self.assertEqual(result, 4)

    # A list of strings that should not be averageable
    def test2(self):
        result = ListAverage.average(["help","is","not","valid"])
        #print(result)
        self.assertEqual(result, "Not a valid list")

    #Invalid empty list
    def test3(self):
        result = ListAverage.average([])
        #print(result)
        self.assertEqual(result, "Not a valid list")

    #Valid float list with negatives
    def test4(self):
        result = ListAverage.average([12.34,-12.34,34.765,-34.765])
        self.assertEqual(result,0)

if __name__ == "__main__":
    unittest.main()