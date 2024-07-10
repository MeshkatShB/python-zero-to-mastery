import unittest
from app import UserDatabase


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.db = UserDatabase()

    def test_add_and_get_user(self):
        self.db.add_user("john_doe", "john@example.com")
        self.assertEqual(self.db.get_user("john_doe"), "john@example.com")

    def test_get_nonexistent_user(self):
        self.assertIsNone(self.db.get_user("nonexistent_user"))


if __name__ == '__main__':
    unittest.main()
