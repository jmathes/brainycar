#!/usr/bin/env python
import os
import time
import logging
from tesla import tesla
from pprint import pprint

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
os.system("rm pidfile")
os.system("echo %s > pidfile" % os.getpid())

def main(car):
    while True:
        time.sleep(1)
        try:
            logging.info("checking %s", car)
            run_all_checks(car)
        except:
            pass

def run_all_checks(car):
    logging.info("awake: %s", car.awake)
    if car.awake:
        logging.info("speed: %s", car.drive_state['speed'])
        current_sunroof_state = car.vehicle_state['sun_roof_percent_open']
        desired_sunroof_state = current_sunroof_state
        if car.drive_state['speed'] >= 45 or car.drive_tate['speed'] is None:
            desired_sunroof_state = 0
        elif car.climate_state['is_auto_conditioning_on']:
            goal = car.climate_state['driver_temp_setting']
            outide = car.climate_state['outside_temp']
            inside = car.climate_state['inside_temp']
            logging.info("Trying to get from %s to %s (%s outside)", inside, goal, outside)
            if (False
                    or (goal < inside and outside < inside)
                    or (goal > inside and outside > inside)
                    ):
                desired_sunroof_state = 100
            else:
                desired_sunroof_state = 0
        if desired_sunroof_state != current_sunroof_state:
            car.sun_roof_control('open' if desired_sunroof_state == 100 else 'close')

if __name__ == "__main__":
    car = tesla.my_car()
    main(car)
