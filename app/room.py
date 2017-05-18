class Room(object):
    """docstring for Room"""

    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type


class Office_space(Room):
    capacity = 6

    def __init__(self, room_name, room_type):
        super(Office_space, self).__init__(room_name, room_type)
        self.room_name = room_name


class Living_quaters(Room):
    capacity = 4

    def __init__(self, room_name, room_type):
        super(Living_quaters, self).__init__(room_name, room_type)
        self.room_name = room_type
