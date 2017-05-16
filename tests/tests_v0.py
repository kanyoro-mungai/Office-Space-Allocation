import unittest

class Testoffice_space(unittest.TestCase):
 class TestCheckClassInheritance(unittest.TestCase):

    def setUp(self):
        self.the_dojo = Dojo()
        
    # check if office is instance of room
    def test_office_is_instance_of_room(self):
        self.office_space = Office()
        self.assertIsInstance(self.office_space, Room)

    # check if living space is instance of room
    def test_livingspace_is_instance_of_room(self):
        self.living_space = LivingSpace()
        self.assertIsInstance(self.living_space,Room)

    # check if fellow is instance of person
    def test_fellow_is_instance_of_person(self):
        self.fellow = Fellow()
        self.assertIsInstance(self.fellow,Person)

    # check if staff is instance of person
    def test_staff_is_instance_of_person(self):
        self.staff = Staff()
        self.assertIsInstance(self.staff, Person)

class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.the_dojo = Dojo()
        self.create_room = create_room()

    # check if room is created
    def test_create_room_successfully(self):
        kilimanjaro_office = self.the_dojo.create_room("blue", "office")
        self.assertTrue(self.blue_office)
        # Test if maximum capacity of the office is 6
    def test_create_room_max_capacity_of_office_is_six(self):
        Simba_office = self.the_dojo.create_room('blue', 'office')
        max_number = self.Simba_office.max_people
        self.assertEqual(max_number, 6)
    # Test if maximum capacity of the living space is 4
    def test_create_room_max_capacity_of_living_space_is_four(self):
        Nzoia_livingspace = self.the_dojo.create_room('black', 'livingspace')
        max_number = self.Nzoia_livingspace.max_people
        self.assertEqual(max_number, 4)
    # Test if you can create mutiple rooms
    def test_create_room_check_multiple_rooms_created(self):
        multiple_offices = self.the_dojo.create_room('yellow','green','bage', 'office')
        self.assertTrue(self.multiple_offices)
    # Test if room already exists


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.the_dojo = Dojo()
        self.add_person = add_person()        
    # check if person is added
    def test_person_add(self):
        new_person = self.the_dojo.add_person('Andrew', 'staff')
        self.assertTrue(self.new_person)
    # check if person_name is a string
    def test_string(self):
        new_person = self.the_dojo.add_person('Simon', 'fellow')
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