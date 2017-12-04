import os, argparse
import enum, json

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

def load_systems(fn):
    print("Loading Systems...")
    systemObj = []
    systemJSON = json.load(open(fn))
    for s in systemJSON:
        systemObj.append( System(s["id"], s["name"]) )
    return systemObj

def load_stations(fn):
    print("Loading Stations...")
    stationObj = []
    stationJSON = json.load(open(fn))
    for s in stationJSON:
        stationObj.append( Station(s["id"], s["name"], s["system_id"], s["type"], s["type_id"], s["is_planetary"]) )
    return stationObj

def find_station(stn_data, sys_data, station, system):
    for stn in stn_data:
        if stn.name == station:
            if stn.system_id:
                for sys in sys_data:
                    if system:
                        if sys.name == system and sys.id == stn.system_id:
                            stn.set_system_name(system)
                            return stn
                    else:
                        if sys.id == stn.system_id:
                            stn.set_system_name(sys.name)
                            return stn


def main():
    system_data  = load_systems("systems_populated.json")
    station_data = load_stations("stations_filtered.json")

    # test
    station = find_station(station_data, system_data, "Jameson Memorial", "Shinrarta Dezhra")
    station.print_info()
    station = find_station(station_data, system_data, "Grant Dock", "Jambe")
    station.print_info()
    station = find_station(station_data, system_data, "Grant Dock", "Li Nang Yi")
    station.print_info()
    station = find_station(station_data, system_data, "Pedersen's Legacy", "Mobia")
    station.print_info()
    station = find_station(station_data, system_data, "The Gnosis", "")
    station.print_info()
    station = find_station(station_data, system_data, "Grant Dock", "")
    station.print_info()
    station = find_station(station_data, system_data, "Teng-hui Station", "Bandjigali")
    station.print_info()

if __name__ == "__main__":
    main()
