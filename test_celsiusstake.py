# test_celsiusstake.py
"""
Tests for CelsiusStake module.
"""

import unittest
from celsiusstake import CelsiusStake

class TestCelsiusStake(unittest.TestCase):
    """Test cases for CelsiusStake class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CelsiusStake()
        self.assertIsInstance(instance, CelsiusStake)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CelsiusStake()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
