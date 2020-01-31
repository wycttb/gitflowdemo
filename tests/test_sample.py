import unittest


class SampleTestSuite(unittest.TestCase):
    """Sample test cases."""

    def test_equal(self):
        assert(1==1)


if __name__ == '__main__':
    unittest.main()