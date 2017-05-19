import unittest
from app.dojo import Dojo


class TestAddPerson(unittest.TestCase):

    def setUp(self):
        self.instance_dojo = Dojo()

    def test_add_Fellow(self):
        number_at_start = len(self.instance_dojo.list_of_fellows)
        self.instance_dojo.add_person('sammy', 'fellow')
        number_after_add = len(self.instance_dojo.list_of_fellows)
        self.assertEqual(number_after_add, number_at_start + 1)

    def test_add_person(self):
        number_at_start = len(self.instance_dojo.list_of_staff)
        self.instance_dojo.add_person('sammy', 'staff')
        number_after_add = len(self.instance_dojo.list_of_staff)
        self.assertEqual(number_after_add, number_at_start + 1)


if __name__ == "__main__":
    unittest.main()
