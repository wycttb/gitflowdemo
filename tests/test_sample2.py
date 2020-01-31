import unittest


class SampleTestSuite2(unittest.TestCase):
    """Sample test cases."""

    def test_neq(self):
        assert(2!=1)

    def test_lt(self):
        assert(1<2)

if __name__ == '__main__':
    unittest.main()