import random
from room import Room, Office_space, Living_quaters
from person import Person, Fellow, Staff


class Dojo(object):

    def __init__(self):
        self.list_of_offices = []
        self.list_of_living_space = []
        self.list_of_staff = []
        self.list_of_fellows = []
        self.list_of_occupants = []

    def create_room(self, room_type, room_name):

        if room_name not in self.list_of_offices and room_name not in self.list_of_living_space:
            if room_type == 'office' or room_type == 'Office':
            # create a new office
              new_o = Office_space(room_name)
              self.list_of_offices.append(room_name)
              print('New Office_space {} created succesfully '.format(room_name))

            elif room_type == 'living' or room_type == 'Living':
             # create a new living
                new_l = Living_quaters(room_name)
                print ('New {}_space is called {}'.format(room_type, room_name))
                self.list_of_living_space.append(room_name)

            else:
                print('Invalid Room Type Use either office or Living as type')

            print(self.list_of_offices)
        else:
            print("sorry... room {} already exists").format(room_name)


    def add_person(self, name, p_type, accomodation='N'):
         if p_type == 'staff' or p_type == 'Staff':
            # create new staff
            new_staff = Staff(name)
            self.list_of_staff.append(name)
                # Assign Office
            r_room = random.choice(self.list_of_offices)
            print('New Staff named {} created successfuly and assigned to {}'.format(name, r_room))
         elif p_type == 'fellow' or p_type == 'Fellow':
            #create new fellow
            new_fellow = Fellow(name)
            self.list_of_fellows.append(name)
             # assign office
            r_room = random.choice(self.list_of_offices)
            print('New Fellow named {0} created successfuly and assigned to office {1}'.format(name, r_room))

            if accomodation == 'y':
                r_living = random.choice(self.list_of_living_space)
                print('New Fellow named {0} has been assigned to living_Space {1}'.format(name, r_living))
         else:
            print ('invalid person type')

