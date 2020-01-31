# -*- coding: utf-8 -*-

from .context import gfdemo

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(gfdemo.hmm())


if __name__ == '__main__':
    unittest.main()
