#!/usr/bin/env python
import os

with open('pidfile', 'rb') as pidfile:
    pid = pidfile.readline()
    print "killing %s" % pid
    os.system("kill %s" % pid)

print os.system("git pull")
print os.system("git submodule update --recursive tesla")
print os.system("nohup ./brainycar.py &")
os.system("ps aux | grep brainycar | grep -v grep")
print "done"
