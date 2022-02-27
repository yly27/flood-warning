from floodsystem.analysis import risk_analysis, risk_rater
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2G"""
    
    stations = build_station_list()
    update_water_levels(stations)

    liszt = risk_analysis(stations)
    print(liszt)
    
    final_list = sorted(liszt.items(), key = lambda x: x[1], reverse = True)
    
    for i in final_list:
        print("Town: {} Risk level: {} Risk rating: {}".format(i[0], i[1], risk_rater(i[1])) )
      

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
