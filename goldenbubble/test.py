from main import *

import unittest

class TestBubble(unittest.TestCase):
    def createt(self, num, size=4):
        return [num for i in range(4)]

    def create_sol(self, num=11):
        tt = []
        for i in range(num):
            tt.append(self.createt(i+1))
        
        for i in range(2):
            tt.append(self.createt(0))

        return tt
    def test_issoln_empty(self):
        tt = self.create_sol()
        self.assertTrue(is_solved(tt))

    def test_issoln_empty_swap(self):
        tt = self.create_sol()
        t1 = tt[0]
        tt[0] = tt[11]
        tt[11] = t1
        self.assertTrue(is_solved(tt))

    def test_issoln_wrong(self):
        tt = self.create_sol()
        tt[0][0] = 0
        self.assertFalse(is_solved(tt))
if __name__ == '__main__':
    unittest.main()