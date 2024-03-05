from functions import add, subtract, is_valid_email, is_weekend
import unittest
from unittest.mock import patch
# import datetime

class TestFunctions(unittest.TestCase):
    # 1.
    def test_add(self):
        self.assertEqual(add(80, 20), 100)

    def test_subtract(self):
        self.assertEqual(subtract(410, 200), 210)
    # 2.
    def test_is_email_valid(self):
        self.assertEqual(is_valid_email('user@host.com'), True)

    def test_is_email_not_valid_user(self):
        self.assertEqual(is_valid_email('userhost.com'), False)

    def test_is_email_not_valid_user_domain(self):
        self.assertEqual(is_valid_email('user@hostcom'), False)

    # 3.
class TestIsWeekend(unittest.TestCase):
    @patch('functions.datetime')
    def test_is_weekend_true(self, mock_is_weekend):
        mock_is_weekend.datetime.today.return_value.strftime.return_value = "Saturday"
        self.assertTrue(is_weekend())

    @patch('functions.datetime')
    def test_is_weekend_false(self, mock_is_weekend):
        mock_is_weekend.datetime.today.return_value.strftime.return_value = "Monday"
        self.assertFalse(is_weekend())

if __name__ == '__main__':
    unittest.main()