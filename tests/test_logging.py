import unittest
from utils.logger import Logger

class TestLogger(unittest.TestCase):
    def test_initialization(self):
        logger = Logger()
        self.assertIsNotNone(logger)

if __name__ == '__main__':
    unittest.main()
