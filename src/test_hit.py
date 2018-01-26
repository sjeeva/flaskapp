import unittest

import hit

class TestHit(unittest.TestCase):
    def test_getServerHitCount(self):
        self.assertEqual(hit.getServerHitCount(), 1)
        self.assertEqual(hit.getServerHitCount(), 2)

if __name__ == '__main__':
    unittest.main()
