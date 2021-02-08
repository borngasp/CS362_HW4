import unittest
import CubeVolume

class CubeVolumeTestCases(unittest.TestCase):

    def test1(self):
        result = CubeVolume.volume(2)
        self.assertEqual(result, 8)

    def test2(self):
        result = CubeVolume.volume("help")
        #print(result)
        self.assertEqual(result, "Not a valid cube")

    def test3(self):
        result = CubeVolume.volume(-2)
        #print(result)
        self.assertEqual(result, "Not a valid cube")

    def test4(self):
        result = CubeVolume.volume(12.34)
        self.assertEqual(result,1879.080904)

if __name__ == "__main__":
    unittest.main()