import unittest

from unittest import TestCase

from SolveEquations import CalcSystemEquals

class TestCalcSystemEqualsWithSolve(TestCase):
    def setUp(self) -> None:
        m = 2
        n = 3
        self.B = [[3, 4, 0, -8],
             [7, 0, 5, -6],
             [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0]]
        
        self.CSE_obj = CalcSystemEquals(m, n, self.B, write_res=False)

    def test_return_searchmin(self):
        d, d_index = self.CSE_obj.SearchMin(index=0)
        self.assertEquals((d, d_index), (3, 0))
    
    def test_calcstring(self):
        self.CSE_obj.CalcString(index=0)
        expected_B = [[1, 0, 0, -8], 
                      [-7, 28, 5, -6], 
                      [-1, 4, 0, 0], 
                      [1, -3, 0, 0], 
                      [0, 0, 1, 0]]
        
        self.assertEquals(self.B, expected_B)
    
    def test_calcequation(self):
        self.CSE_obj.CalcEquation()
        expected_B = [[1, 0, 0, 0], 
                      [-7, 1, 0, 0], 
                      [-1, 8, -20, 488], 
                      [1, -6, 15, -364], 
                      [0, -11, 28, -682]]
        
        self.assertEquals(self.B, expected_B)


class TestCalcSystemEqualsWithoutSolve(TestCase):
    def setUp(self) -> None:
        m = 2
        n = 3
        self.B = [[3, 6, 0, -8],
             [7, 0, 5, -6],
             [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0]]
        
        self.CSE_obj = CalcSystemEquals(m, n, self.B, write_res=False)
    
    def test_calcequation(self):
        self.assertRaises(ValueError, self.CSE_obj.CalcEquation)



class TestCalcSystemEqualsWith4x4martix(TestCase):
    def setUp(self) -> None:
        m = 2
        n = 3
        self.B = [
             [3, 6, 0, 3, -8],
             [7, 0, 5, 4, -6],
             [4, 3, 4, 2, -6],
             [1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0]]
        
        self.CSE_obj = CalcSystemEquals(m, n, self.B)
    


class TestCalcSystemEqualsWith0x0martix(TestCase):
    def setUp(self) -> None:
        m = 2
        n = 3
        self.B = [[]]
        
        self.CSE_obj = CalcSystemEquals(m, n, self.B)

    def test_calcequation(self):
        self.assertRaises(Exception, self.CSE_obj.CalcEquation)



if __name__ == "__main__":
    unittest.main()