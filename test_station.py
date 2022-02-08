# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from test_geo import tester_station


def test_typical_range_consistent():
    assert tester_station[0].typical_range_consistent() == False
    assert tester_station[1].typical_range_consistent() == True