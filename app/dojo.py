import random
from room import Office_space, Living_quaters
from person import Fellow, Staff


class Dojo(object):

    def __init__(self):
        self.unallocated = []
        self.list_of_offices = {}
        self.list_of_living_space = {}
        self.list_of_staff = []
        self.list_of_fellows = []

    def create_room(self, room_type, room_name):
        room_type = room_type.lower()
        if room_name not in self.list_of_offices and room_name not in self.list_of_living_space:

            if room_type == 'office':
                # create a new office
                new_office = Office_space(room_name, room_type)
                self.list_of_offices[room_name] = []
                print('\n')
                print('______________Office Created __________')
                print('New Office {} created succesfully'.format(room_name))

            elif room_type == 'living':
                # create a new living
                new_l = Living_quaters(room_name, room_type)
                self.list_of_living_space[room_name] = []
                print('\n')
                print('______________Living Space Created __________')
                print('New Living_space is called {}'
                      .format(room_name.upper()))

            else:
                print('Invalid Room Type Use either office or Living as type')

        else:
            print("sorry... room {} already exists").format(room_name.upper())

    def allocate_office_space(self, name):
        try:
            random_room = random.choice(list(self.list_of_offices))
            if(len(self.list_of_offices[random_room])) < Office_space.capacity:
                self.list_of_offices[random_room].append(name)
                print('\n')
                print('______________Office Space Allocation__________')
                print('{} has been assigned to {} office space'.format(
                    name.upper(), random_room.upper()))
            else:
                self.allocate_office_space(name)
        except:
            self.unallocated.append(name)
            print('______________Unallocation __________')
            print('No office space available {} has been put in a waiting list'
                  .format(name.upper()))

    def allocate_living_space(self, name):
        try:
            random_room = random.choice(list(self.list_of_living_space))
            if(len(self.list_of_living_space[random_room])) < Living_quaters.capacity:
                self.list_of_living_space[random_room].append(name)
                print('\n')
                print('______________Living Space Allocation__________')
                print('{} has been assigned to {} living space'.format(
                    name.upper(), random_room.upper()))
            else:
                self.allocate_living_space(name)
        except:
            self.unallocated.append(name)
            print('______________Unallocation __________')
            print('No living space available {} has been put in a waiting list'
                  .format(name.upper()))

    def add_person(self, name, p_type, accomodation='N'):
        p_type = p_type.lower()
        accomodation = accomodation.lower()

        if p_type == 'staff':
            # create new staff
            new_staff = Staff(name, accomodation)
            self.list_of_staff.append(name)
            print('\n')
            print('______________STAFF__________')
            print('New Staff named {} created successfuly'
                  .format(name.upper()))
            self.allocate_office_space(name)

            if (accomodation == 'y'):
                print('\n')
                print('______________Living Space Allocation__________')
                print('Sorry Living space not available for staff')

        elif p_type == 'fellow':
            # create new fellow
            new_fellow = Fellow(name)
            self.list_of_fellows.append(name)
            print('\n')
            print('______________FELLOW__________')
            print('New Fellow named {} created'.format(name.upper()))
            print('\n')

            self.allocate_office_space(name)

            if accomodation == 'y':
                self.allocate_living_space(name)
        else:
            print('invalid person type')
