class System(object):
    def __init__(self, _id, _name):
        self.id = _id
        self.name = _name

class Station(object):
    def __init__(self, _id, _name, _system_id, _type, _type_id, _is_planetary):
        self.id = _id
        self.name = _name
        self.system_id = _system_id
        self.type = _type
        self.type_id = _type_id
        self.is_planetary = _is_planetary
        self.system_name = ""

    def set_system_name(self, _system):
        self.system_name = _system

    def docking_pad_layout(self):
        if self.is_planetary:
            return 0
        if self.type_id in [3,7,8,12,20]:	# Starports, Asteroid Base
            return 1
        if self.type_id in [1,2,4,5,6,9,11,13]: # Outposts
            return 2
        return 0                                # Unknown

    def print_info(self):
        if self.type:
            print("Station " + self.name + " at " + self.system_name + ", " + self.type + ", layout: " + str(self.docking_pad_layout()))
        else:
            print("Station " + self.name)
