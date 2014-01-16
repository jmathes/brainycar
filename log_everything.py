#!/usr/bin/env python
import os
import time
import logging
import json
from tesla import tesla
from pprint import pprint

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

all_state_values = {}

def main(car):
    last_dump = 0
    while True:
        time.sleep(1)
        try:
            run_all_checks(car)
            if time.time() - last_dump > 300:
                logging.info(json.dumps(all_state_values))
                last_dump = time.time()
        except:
            pass

def run_all_checks(car):
    for category in car.car_state:
        if category not in all_state_values:
            all_state_values[category] = {}
        current = car.__getattribute__(category)
        for k, v in current.iteritems():
            rv = v.__repr__()
            if k not in all_state_values[category]:
                all_state_values[category][k] = []
            if rv not in all_state_values[category][k]:
                all_state_values[category][k].append(rv)
            for k in all_state_values[category]:
                if k not in current and '(not present)' not in all_state_values[category][k]:
                    all_state_values[category][k].append('(not present)')

if __name__ == "__main__":
    car = tesla.my_car()
    main(car)
    # run_all_checks(car)
    # pprint(all_state_values)
