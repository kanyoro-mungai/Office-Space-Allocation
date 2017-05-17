class Room(object):
	"""docstring for Room"""
	def __init__(self,room_name, room_type, capacity):
		self.room_name = room_name
		self.room_type  = room_type
		self.capacity = capacity
		self.occupants = []

	
		
class Office_space(Room):
	"""docstring for Office_space"""
	def __init__(self, room_name):
		super(Office_space, self).__init__(room_name, room_type = 'office', capacity = 6)

		

		
class Living_quaters(Room):
	"""docstring for Living_quaters"""
	def __init__(self, room_name):
		super(Living_quaters, self).__init__(room_name, room_type = "living Quaters", capacity = 4 )


		
		
			
			