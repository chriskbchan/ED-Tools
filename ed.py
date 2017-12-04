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

    def docking_assist(self):
        if self.is_planetary:
            return False
        if self.type_id in [3,7,8,12,20]:	# Starports, Asteroid Base
            return True
        return False

    def print_info(self):
        if self.type:
            print("Station " + self.name + " at " + self.system_name + ", type " + self.type + ", docking assist " + str(self.docking_assist()))
        else:
            print("Station " + self.name)
