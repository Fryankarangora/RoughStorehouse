# test_roughstorehouse.py
"""
Tests for RoughStorehouse module.
"""

import unittest
from roughstorehouse import RoughStorehouse

class TestRoughStorehouse(unittest.TestCase):
    """Test cases for RoughStorehouse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughStorehouse()
        self.assertIsInstance(instance, RoughStorehouse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughStorehouse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
