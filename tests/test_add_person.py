import unittest
from app.dojo import Dojo
from app.room import Room, Office_space, Living_quaters
from app.person import Person, Staff, Fellow

instance_dojo = Dojo()

class TestAddPerson(unittest.TestCase):

    def test_add_Fellow(self):
        number_at_start = len(instance_dojo.list_of_fellows)
        instance_dojo.add_person('sammy', 'fellow')
        number_after_add =len(instance_dojo.list_of_fellows)
        self.assertEqual(number_after_add, number_at_start + 1)


    def test_add_person(self):
        number_at_start = len(instance_dojo.list_of_staff)
        instance_dojo.add_person('sammy', 'staff')
        number_after_add = len(instance_dojo.list_of_staff)
        self.assertEqual(number_after_add, number_at_start + 1)

    if __name__ == "__main__":
     unittest.main()