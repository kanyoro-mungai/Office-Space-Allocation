import random
from room import Room, Office_space, Living_quaters
from person import Person, Fellow, Staff


class Dojo(object):
    def __init__(self):
        self.list_of_offices = []
        self.list_of_living_space= []
        self.list_of_staff = []
        self.list_of_fellows = []
        self.list_of_occupants = []



    def create_room(self, room_name, room_type):
        
        for room_name in room_name.split():

            if room_name in self.list_of_offices or room_name in self.list_of_living_space:
                print("sorry... room {} already exists").format(room_name)
            else:

                if room_type == 'office' or room_type == 'Office':
                    # create a new office
                    new_o = Office_space(room_name)
                    self.list_of_offices.append(new_o)

                    print('New Office_space {} created succesfully '.format(room_name))

                   # print(self.list_of_offices)




                elif room_type == 'living' or room_type == 'Living':
                    # create a new living
                    new_l = Living_quaters(room_name)
                    print 'New {}_space is called {}'.format(room_type, room_name)

                    self.list_of_living_space.append(new_l)

                   # print(self.list_of_living_space)

                else:
                    print('Invalid Room Type Use either office or Living as type')


    def add_person(self, name, p_type, accomodation = 'N'):

        if p_type == 'staff' or p_type == 'Staff':
            #create new staff
            new_staff = Staff(name)
            self.list_of_staff.append(new_staff)
            #Assign Office
            r_room = random.choice(self.list_of_offices)
            #r_room.occupants.append(new_staff)

            print ('New Staff named {0} created successfuly and assigned to {1}'.format(name, r_room.room_name))

            

        elif p_type == 'fellow' or p_type == 'Fellow':
            new_fellow = Fellow(name)
            self.list_of_fellows.append(new_fellow)
            #assign office
            r_room = random.choice(self.list_of_offices)
            print ('New Fellow named {0} created successfuly and assigned to office {1}'.format(name, r_room.room_name))

            if accomodation == 'y':
                 r_living = random.choice(self.list_of_living_space)
                 print ('New Fellow named {0} has been assigned to living_Space {1}'.format(name, r_living.room_name))

        else:
            print 'invalid person type'


    # def assign_room(self):
    #     for room in self.list_of_offices:
    #         print (room.room_name, room.room_type, room.capacity)

    #     pass


# newDojo = Dojo()
# newDojo.create_room('office', 'black blue green yellow white')
# newDojo.create_room('living', 'Wet Dry moist')

# newDojo.add_person('george', 'fellow', 'y')

