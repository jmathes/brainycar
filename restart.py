#!/usr/bin/env python
import os

with open('pidfile', 'rb') as pidfile:
    pid = pidfile.readline()
    print "killing %s" % pid
    os.system("kill %s" % pid)

os.system("git pull origin master")
os.system("git submodule update --recursive tesla")
os.system("nohup ./brainycar.py &")
