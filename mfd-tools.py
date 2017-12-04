from ed import *
import json

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
    test_data = [ ("Jameson Memorial", "Shinrarta Dezhra"),
                  ("Grant Dock", "Jambe"),
                  ("Grant Dock", "Li Nang Yi"),
                  ("Pedersen's Legacy", "Mobia"),
                  ("The Gnosis", ""),
                  ("Grant Dock", ""),
                  ("Teng-hui Station", "Bandjigali") ]
    for (stn, sys) in test_data:
        station = find_station(station_data, system_data, stn, sys)
        station.print_info()

if __name__ == "__main__":
    main()
