import unittest
from slackbot import utils


class TestUtils(unittest.TestCase):
    def test_is_int(self):
        result = utils.is_number(100)
        self.assertTrue(result, True)

        result = utils.is_number(-100)
        self.assertTrue(result, True)

        result = utils.is_number(10.98)
        self.assertTrue(result, True)

        result = utils.is_number(-10.32)
        self.assertTrue(result, True)


if __name__ == '__main__':
    unittest.main()
