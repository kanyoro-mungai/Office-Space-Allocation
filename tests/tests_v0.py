import unittest
from app.dojo import Dojo
from app.room import Room, Office_space, Living_quaters
from app.person import Person, Staff, Fellow



class TestCheckClassInheritance(unittest.TestCase):
    # check if office is instance of room
    def test_office_is_instance_of_room(self):
        blue_office = Room('blue', 'office', 6 )
        self.assertIsInstance(blue_office, Room)

    # check if living space is instance of room
    def test_livingquaters_is_instance_of_room(self):
        blue_living = Room('red', 'living Quaters', 4)
        self.assertIsInstance(blue_living, Room)

    # check if fellow is instance of person
    def test_fellow_is_instance_of_person(self):
        new_fellow = Fellow('George', 'fellow')
        self.assertIsInstance(new_fellow, Fellow)

    # check if staff is instance of person
    def test_staff_is_instance_of_person(self):
        new_staff = Staff('George', 'Staff')
        self.assertIsInstance(new_staff, Person)


class TestCreateRoom(unittest.TestCase):

    # check if room is created
    def test_create_room_successfully(self):
        instance_dojo = Dojo()
        blue_office = instance_dojo.create_room('blue', 'office')
        self.assertEqual(blue_office, 'New office_space is called blue')
        # Test if maximum capacity of the office is 6
    def test_create_room_max_capacity_of_office_is_six(self):
        blue_office = self.newdojo.create_room('blue', 'office')
        space = self.blue_office.space
        self.assertEqual(space, 6)
    # Test if maximum capacity of the living space is 4
    def test_create_room_max_capacity_of_living_space_is_four(self):
        black_livingspace = self.the_dojo.create_room('black', 'livingspace')
        space = self.black_livingspace.space
        self.assertEqual(space, 4)
    Test if room already exists


class TestAddPerson(unittest.TestCase):
    # check if person is added
    def test_person_add(self):
        instance_dojo = Dojo()
        new_person = instance_dojo.add_person('Andrew', 'Staff')
        self.assertEqual(new_person, 'New Staff named Andrew created successfuly')

    # check if person_name is a string
    def test_string(self):
        instance_dojo = Dojo()
        new_person = instance_dojo.add_person('Simon', 'fellow')
        self.assertIsInstance(new_person, str)
    # check if room is allocated
    def test_room(self):
        new_person =self.the_dojo.add_person('Charles', 'staff')
        allocate_room = self.new_person.allocate_room()
        self.assertTrue(self.allocate_room)
    # add a staff member and check if type of person is staffperson
    def test_staff(self):
        new_staff_member =self.the_dojo.add_person('Brenda','staff')
        self.assertIsInstance(self.new_staff_member, Staff)
    # add fellow who wants accomodation. check if living space is allocated
    def test_living_space(self):
        new_fellow = self.the_dojo.add_person('Muna' 'fellow')
        allocate_room = self.new_fellow.allocate_room()
        self.assertTrue(self.allocate_room)


    if __name__ == "__main__":
     unittest.main()