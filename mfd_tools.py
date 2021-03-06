from ed import *
from ed_journal import *
import argparse
import json
import random

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

def show_landing_pad(station, pad_id):
    pad_layout = station.docking_pad_layout()
    if pad_layout == 1:
        pad_info = station.coriolis_pad_info(pad_id)
        print("Landing pad %d (%s) at %d o'clock %s" %
            (pad_id, Station.PAD_SIZE_DESC[pad_info[2]], pad_info[0], Station.PAD_DEPTH_DESC[pad_info[1]]) )
    if pad_layout == 2:
        pad_info = station.outpost_pad_info()
        for p in pad_info:
            print("Landing pad schema URL: %s%s" % (Station.EDDB_IMG_BASEURL,p))

# main

def main(args):
    # test station
    if args.function == "station":
        system_data  = load_systems("systems_populated.json")
        station_data = load_stations("stations_filtered.json")

        test_data = [ ("Jameson Memorial", "Shinrarta Dezhra"),
                      ("Grant Dock", "Jambe"),
                      ("Grant Dock", "Li Nang Yi"),
                      ("Pedersen's Legacy", "Mobia"),
                      ("The Gnosis", ""),
                      ("Grant Dock", ""),
                      ("Fowler Platform", "Apian Yi"),
                      ("Teng-hui Station", "Bandjigali") ]
        for (stn, sys) in test_data:
            station = find_station(station_data, system_data, stn, sys)
            station.print_info()
            show_landing_pad(station, random.randrange(40) + 1)

    # test journal
    if args.function == "journal":
        jfn = journal_last_updated(args.path_to_journal)
        if jfn:
            print("Lastest journal file = " + jfn)
            events = [ "DockingGranted", "Location" ]
            journal_show_events(args.path_to_journal, events)
        else:
            print("No journal file found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="Function to test: [station, journal]")
    parser.add_argument("-p", help="path of journal directory", action="store", dest="path_to_journal")
    args = parser.parse_args()
    main(args)
