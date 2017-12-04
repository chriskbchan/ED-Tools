class System(object):
    def __init__(self, _id, _name):
        self.id = _id
        self.name = _name

class Station(object):
    COR_PAD_CLOCK = [ 0,                                   # direction at N o'clock
        6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 11,    #  1 - 20
        11, 11, 11, 12, 12, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4 ]   # 21 - 40
    COR_PAD_DEPTH = [ 0,                                   # 1: Near, 2: Mid, 3: Far
        1, 1, 3, 3, 1, 1, 2, 3, 1, 3, 1, 1, 2, 3, 3, 1, 1, 3, 3, 1,         #  1 - 20
        1, 2, 3, 1, 3, 1, 1, 2, 3, 3, 1, 1, 3, 3, 1, 1, 2, 3, 1, 3 ]        # 21 - 40
    COR_PAD_SIZE  = [ 0,                                   # 1: small, 2: medium, 3: large
        1, 3, 2, 1, 2, 1, 2, 2, 3, 3, 2, 1, 1, 1, 2, 1, 3, 2, 1, 2,         #  1 - 20
        1, 2, 2, 3, 3, 2, 1, 1, 1, 2, 1, 3, 2, 1, 2, 1, 2, 2, 3, 3 ]        # 21 - 40
    PAD_DEPTH_DESC = [ "undefined", "near", "mid", "far" ]
    PAD_SIZE_DESC  = [ "undefined", "small", "medium", "large" ]

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
        if self.type_id in [1,2,4,5,6,9]: 	# Outposts w/ image
            return 2
        if self.type_id in [11]: 		# Outposts w/o image
            return 3
        return 0                                # Unknown

    def coriolis_pad_info(self, pad_id):
        return ( self.COR_PAD_CLOCK[pad_id], self.COR_PAD_DEPTH[pad_id], self.COR_PAD_SIZE[pad_id] )

    def print_info(self):
        if self.type:
            print("Station " + self.name + " at " + self.system_name + ", " + self.type + ", layout: " + str(self.docking_pad_layout()))
        else:
            print("Station " + self.name)
