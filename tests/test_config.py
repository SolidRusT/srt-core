import unittest
from config.config import Config

class TestConfig(unittest.TestCase):
    def test_initialization(self):
        config = Config()
        self.assertIsNotNone(config)

if __name__ == '__main__':
    unittest.main()
