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



    def create_room(self, room_type, room_name):
        for room_name in room_name.split():

            if room_name in self.list_of_offices or room_name in self.list_of_living_space:
                print("sorry... room {} already exists").format(room_name)
            else:

                if room_type == 'office' or room_type == 'Office':
                    # create a new office
                    new_o = Office_space(room_name)
                    self.list_of_offices.append(new_o)

                    print('New {}_space is called {}'.format(room_type, room_name))

                    print(self.list_of_offices)




                elif room_type == 'living' or room_type == 'Living':
                    # create a new living
                    new_l = Living_quaters(room_name)
                    print 'New {}_space is called {}'.format(room_type, room_name)

                    self.list_of_living_space.append(new_l)

                    print(self.list_of_living_space)

                else:
                    print('Invalid Room Type Use either office or Living as type')

    def add_person(self, name, p_type):

        if p_type == 'staff' or p_type == 'Staff':
        	#create new staff
        	new_staff = Staff(name)
        	self.list_of_staff.append(new_staff)
        	#Assign Office
        	r_room = random.choice(self.list_of_offices)

            	print ('New Staff named {0} created successfuly and assigned to {1}'.format(name, r_room.room_name))

            

        elif p_type == 'fellow' or p_type == 'Fellow':
        	new_fellow = Fellow(name)
            print 'New Fellow named {} created successfuly'.format(name)

        else:
            print 'invalid person type'


    def assign_room(self):
    	for room in self.list_of_offices:
    		print (room.room_name, room.room_type, room.capacity)

    	pass


newDojo = Dojo()
newDojo.create_room('office', 'black blue green yellow white')
newDojo.add_person('george', 'staff')
