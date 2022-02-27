#Import test data
from test_geo import tester_station
from floodsystem.flood import stations_level_over_threshold

'''Task 2B Test (Part 2)'''
tester_station[1].latest_level = 20
test_list = stations_level_over_threshold(tester_station, 0.5)

for i in range (len(test_list)):
    assert test_list[i][1] > 0.5