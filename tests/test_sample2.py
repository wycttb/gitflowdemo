import unittest


class SampleTestSuite(unittest.TestCase):
    """Sample test cases."""

    def test_neq(self):
        assert(2!=1)


if __name__ == '__main__':
    unittest.main()