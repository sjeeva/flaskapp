import unittest
import utils
import socket

class TestUtils(unittest.TestCase):
    def test_gethostname(self):
        self.assertNotEqual(utils.gethostname(), "")

    def test_getlocaladdress(self):
        self.assertTrue(socket.inet_aton(utils.getlocaladdress()))

if __name__ == '__main__':
    unittest.main()
