

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    '''Build list of stations'''
    stations = build_station_list()
    p = (52.2053, 0.1218)

    distance_list_sorted = stations_by_distance(stations, p)

    close = distance_list_sorted[:10]
    far = distance_list_sorted[-10:]
    print("10 closest stations to Cambridge city centre are: {}" .format(close))
    print("10 furthest stations to Cambridge city centre are: {}" .format(far))

    


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()