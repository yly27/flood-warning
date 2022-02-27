from floodsystem.analysis import risk_analysis
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 2G"""
    
    stations = build_station_list()
    #for station in risk_analysis(stations):
    #    print("station {} risk level {}".format((station[0]).name, station[1]))

    print(risk_analysis(stations))
      

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
