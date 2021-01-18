from django.test import TestCase
from app.calculator import add, sub

class CalcTests(TestCase):
    def test_add_num(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8), 11)


    def test_sub_num(self):
        """Test sub two nums"""
        self.assertEqual(sub(5,1),4)