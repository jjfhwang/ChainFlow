# test_chainflow.py
"""
Tests for ChainFlow module.
"""

import unittest
from chainflow import ChainFlow

class TestChainFlow(unittest.TestCase):
    """Test cases for ChainFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainFlow()
        self.assertIsInstance(instance, ChainFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
