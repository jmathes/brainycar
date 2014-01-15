#!/usr/bin/env python
import os
import time

with open('pidfile', 'rb') as pidfile:
    pid = pidfile.readline()
    time.sleep(1)
    print "killing %s" % pid
    time.sleep(1)
    os.system("kill %s" % pid)

time.sleep(1)
print os.system("git pull")
time.sleep(1)
print os.system("git submodule update --recursive tesla")
time.sleep(1)
print os.system("nohup ./brainycar.py &")
time.sleep(1)
os.system("ps aux | grep brainycar | grep -v grep | grep -v restart")
time.sleep(1)
print "done"
time.sleep(1)
