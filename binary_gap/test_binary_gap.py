import unittest
from binary_gap import solution

class TestBinaryGap(unittest.TestCase):
    
    def test_examples(self):
        self.assertEqual(solution(9), 2)         # 1001 → gap = 2
        self.assertEqual(solution(529), 4)       # 1000010001 → gaps = 4, 3
        self.assertEqual(solution(20), 1)        # 10100 → gap = 1
        self.assertEqual(solution(15), 0)        # 1111 → no gap
        self.assertEqual(solution(32), 0)        # 100000 → no gap
        self.assertEqual(solution(1041), 5)      # 10000010001 → gap = 5

    def test_edge_cases(self):
        self.assertEqual(solution(1), 0)         # 1 → no gap
        self.assertEqual(solution(0b101010), 1)  # alternating 1s and 0s → max gap = 1
        self.assertEqual(solution(0b1000001), 5) # gap of 5
        self.assertEqual(solution(0b10001), 3)   # gap = 3
        self.assertEqual(solution(0b10000000001), 9) # large gap

    def test_large_input(self):
        self.assertEqual(solution(2**30 + 1), 29) # 1 followed by 29 zeros then 1 → gap = 29
        self.assertEqual(solution(2_147_483_647), 0) # all 1s in binary → no gap

if __name__ == '__main__':
    unittest.main()

