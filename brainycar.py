#!/usr/bin/env python
import os
from tesla import tesla
from pprint import pprint

grace = tesla.my_car()
print grace.asleep
pprint(grace.diagnostic())


def main(car):
    while True:
        time.sleep(1)
        try:
            run_all_checks(car)
        except:
            pass

def run_all_checks():
    if not car.asleep:
        if car.drive_state['speed'] > 45:
            car.sun_roof_control('close')


if __name__ == "__main__":
    car = tesla.tesla.my_car()
    main()
