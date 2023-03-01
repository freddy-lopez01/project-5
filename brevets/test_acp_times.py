"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def brevet_test1():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    distance = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours= 1, minutes=28), start_time.shift(hours = 3, minutes= 30)),
        100: (start_time.shift(hours= 2, minutes=56), start_time.shift(hours= 6, minutes= 40)),
        150: (start_time.shift(hours= 4, minutes=25), start_time.shift(hours= 10, minutes= 0)),
        200: (start_time.shift(hours= 5, minutes=53), start_time.shift(hours= 13, minutes=30))
        }
    for km, time_tuple in checkpoints.items():
        o_time, c_time = time_tuple
        assert(open_time(km, distance, start_time) == o_time)
        assert(close_time(km, distance, start_time) == c_time)

def brevet_test2():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    distance = 300
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        80: (start_time.shift(hours= 2, minutes=21), start_time.shift(hours = 5, minutes= 20)),
        160: (start_time.shift(hours= 4, minutes=42), start_time.shift(hours= 10, minutes= 40)),
        240: (start_time.shift(hours= 7, minutes=8), start_time.shift(hours= 16, minutes= 0)),
        300: (start_time.shift(hours= 9, minutes=0), start_time.shift(hours= 20, minutes=0))
        }
    for km, time_tuple in checkpoints.items():
        o_time, c_time = time_tuple
        assert(open_time(km, distance, start_time) == o_time)
        assert(close_time(km, distance, start_time) == c_time)

def brevet_test3():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    distance = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        30: (start_time.shift(minutes=53), start_time.shift(hours = 2, minutes= 30)),
        60: (start_time.shift(hours= 1, minutes=46), start_time.shift(hours= 4, minutes=0)),
        90: (start_time.shift(hours= 2, minutes=39), start_time.shift(hours= 6, minutes= 0)),
        120: (start_time.shift(hours=3 , minutes=32), start_time.shift(hours= 8, minutes=0)),
        150: (start_time.shift(hours=4 , minutes=25), start_time.shift(hours= 10, minutes=0)),
        180: (start_time.shift(hours=5 , minutes=18), start_time.shift(hours= 12, minutes=0)),
        200: (start_time.shift(hours=5 , minutes=53), start_time.shift(hours= 13, minutes=30))
        }
    for km, time_tuple in checkpoints.items():
        o_time, c_time = time_tuple
        assert(open_time(km, distance, start_time) == o_time)
        assert(close_time(km, distance, start_time) == c_time)

def brevet_test4():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    distance = 400
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours= 1, minutes=28), start_time.shift(hours = 3, minutes= 30)),
        100: (start_time.shift(hours= 2, minutes=56), start_time.shift(hours= 6, minutes= 40)),
        200: (start_time.shift(hours= 5, minutes=53), start_time.shift(hours= 13, minutes= 20)),
        300: (start_time.shift(hours= 9, minutes=0), start_time.shift(hours= 20, minutes=0)),
        400: (start_time.shift(hours= 12, minutes=8), start_time.shift(hours= 27, minutes=0))
        }
    for km, time_tuple in checkpoints.items():
        o_time, c_time = time_tuple
        assert(open_time(km, distance, start_time) == o_time)
        assert(close_time(km, distance, start_time) == c_time)

def brevet_test5():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    distance = 1000
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        100: (start_time.shift(hours= 2, minutes=56), start_time.shift(hours = 6, minutes= 40)),
        200: (start_time.shift(hours= 5, minutes=53), start_time.shift(hours= 13, minutes= 20)),
        400: (start_time.shift(hours= 12, minutes=8), start_time.shift(hours= 26, minutes= 40)),
        600: (start_time.shift(hours= 18, minutes=48), start_time.shift(hours= 40, minutes=0)),
        800: (start_time.shift(hours= 25, minutes=57), start_time.shift(hours= 57, minutes=30)),
        1000: (start_time.shift(hours= 33, minutes=5), start_time.shift(hours= 75, minutes=0))
        }
    for km, time_tuple in checkpoints.items():
        o_time, c_time = time_tuple
        assert(open_time(km, distance, start_time) == o_time)
        assert(close_time(km, distance, start_time) == c_time)