#!/usr/bin/env python
import os
import time
import logging
from tesla import tesla
from pprint import pprint

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
os.system("rm pidfile")
os.system("echo %s > pidfile" % os.getpid())
os.system("cat pidfile")

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
        if car.drive_state['speed'] >= 45 or True:
            car.sun_roof_control('close')


if __name__ == "__main__":
    car = tesla.my_car()
    main(car)
