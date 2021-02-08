import unittest
import CubeVolume

class CubeVolumeTestCases(unittest.TestCase):

    #A valid int test
    def test1(self):
        result = CubeVolume.volume(2)
        self.assertEqual(result, 8)

    #An invalid string value for x
    def test2(self):
        result = CubeVolume.volume("help")
        #print(result)
        self.assertEqual(result, "Not a valid cube")

    #An invalid negative sized cube
    def test3(self):
        result = CubeVolume.volume(-2)
        #print(result)
        self.assertEqual(result, "Not a valid cube")

    #A valid float sized cube
    def test4(self):
        result = CubeVolume.volume(12.34)
        self.assertEqual(result,1879.080904)

if __name__ == "__main__":
    unittest.main()