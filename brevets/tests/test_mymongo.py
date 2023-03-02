"""
Nose tests for mymongo.py

Write your tests HERE AND ONLY HERE.
"""
from mymongo import insert_brevet, get_brevet
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def mymongo_test_insert():
    """
    Test inserting values into data base
    """
    #copied from test_acp_times.py
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    distance = 200
    checkpoints = [
        {"miles": 0, "km":0, "open":str(start_time), "close": str(start_time.shift(hours = 1)), "location": "start"},
        {"miles": 31.0686, "km":50, "open": str(start_time.shift(hours= 1, minutes=28), "close":start_time.shift(hours = 3, minutes= 30)), "location": "control1"},
        {"miles": 62.1371, "km":100, "open": str(start_time.shift(hours= 2, minutes=56), "close":start_time.shift(hours = 6, minutes= 40)), "location": "control2"},
        {"miles": 93.2057, "km":150, "open": str(start_time.shift(hours= 4, minutes=25), "close":start_time.shift(hours = 10, minutes= 0)), "location": "control3"},
        {"miles": 124.274, "km":200, "open": str(start_time.shift(hours= 5, minutes=53), "close":start_time.shift(hours = 13, minutes= 30)), "location": "control4"},        
        
        
        #100: (start_time.shift(hours= 2, minutes=56), start_time.shift(hours= 6, minutes= 40)),
        #150: (start_time.shift(hours= 4, minutes=25), start_time.shift(hours= 10, minutes= 0)),
        #200: (start_time.shift(hours= 5, minutes=53), start_time.shift(hours= 13, minutes=30))
    ]
    insert_res = insert_brevet(str(start_time), distance, checkpoints)
    assert isinstance(brevet_insert_id, str) and len(brevet_insert_id) > 0 

def mymondo_test_fetch():
    pass
