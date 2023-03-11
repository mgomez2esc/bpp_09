from funciones import calcula_media
import unittest

class Test_misfunciones(unittest.TestCase):
    def test_01(self):
        result = calcula_media([5,5,5])
        self.assertEqual(result, 5)

    def test_02(self):
        result = calcula_media([5,5,5])
        self.assertEqual(result, 15)    

unittest.main()

