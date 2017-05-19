import unittest
from app.room import Room
from app.person import Person, Staff, Fellow


class TestCheckClassInheritance(unittest.TestCase):
    # check if office is instance of room

    def test_office_is_instance_of_room(self):
        blue_office = Room('blue', 'office')
        self.assertIsInstance(blue_office, Room)

    # check if living space is instance of room
    def test_livingquaters_is_instance_of_room(self):
        blue_living = Room('red', 'living Quaters')
        self.assertIsInstance(blue_living, Room)

    # check if fellow is instance of person
    def test_fellow_is_instance_of_person(self):
        new_fellow = Fellow('George', 'fellow')
        self.assertIsInstance(new_fellow, Fellow)

    # check if staff is instance of person
    def test_staff_is_instance_of_person(self):
        new_staff = Staff('George', 'Staff')
        self.assertIsInstance(new_staff, Person)


if __name__ == "__main__":
    unittest.main()
