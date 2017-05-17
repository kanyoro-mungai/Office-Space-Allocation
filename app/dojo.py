from room import Room, Office_space, Living_quaters


class Dojo(object):
    def __init__(self):
        pass

    def create_room(self, room_type, room_name):
        # creates  a room list
        list_of_rooms = ["blue"]
        for room_name in room_name.split():

            if room_name in list_of_rooms:
                print("sorry... room {} already exists").format(room_name)
            else:

                if room_type == 'office' or room_type == 'Office':
                    # create a new office
                    new_o = Office_space(room_name)
                    list_of_rooms.append(new_o.room_name)

                    print('New {}_space is called {}'.format(room_type, room_name))


                elif room_type == 'living' or room_type == 'Living':
                    # create a new living
                    new_l = Living_quaters(room_name)
                    print 'New {}_space is called {}'.format(room_type, room_name)

                    list_of_rooms.append(room_name)

                    print(list_of_rooms)

                else:
                    print('Invalid Room Type Use either office or Living as type')

    def add_person(self, name, p_type):

        if p_type == 'staff' or p_type == 'Staff':
            print 'New Staff named {} created successfuly'.format(name)
            # my_list = list_of_office

            # print random.choice(my_list)

        elif p_type == 'fellow' or p_type == 'Fellow':
            print 'New Fellow named {} created successfuly'.format(name)

        else:
            print 'invalid person type'


newDojo = Dojo()
newDojo.create_room('living', 'blue green pink')
