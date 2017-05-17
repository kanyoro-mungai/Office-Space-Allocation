import unittest
from app.dojo import Dojo

instance_dojo = Dojo()

class TestCreateRoom(unittest.TestCase):

    # check if office is created
    def test_create_office(self):
        no_on_start = len(instance_dojo.list_of_offices)
        instance_dojo.create_room('blue', 'office')
        no_after_creation = len(instance_dojo.list_of_offices)
        self.assertEqual(no_after_creation, no_on_start + 1)
    # add living Space

    def test_create_living(self):
        no_on_start = len(instance_dojo.list_of_living_space)
        instance_dojo.create_room('yellow', 'living')
        no_after_creation = len(instance_dojo.list_of_living_space)
        self.assertEqual(no_after_creation, no_on_start + 1)

    if __name__ == "__main__":
     unittest.main()