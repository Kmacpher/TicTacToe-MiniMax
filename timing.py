# File: timing-example-2.py

import time, sys

if sys.platform == "win32":
    timer = time.clock
else:
    timer = time.time

t0 = t1 = 0

def start():
    global t0
    t0 = timer()

def finish():
    global t1
    t1 = timer()

def seconds():
    return int(t1 - t0)

def milli():
    return int((t1 - t0) * 1000)

def micro():
    return int((t1 - t0) * 1000000)
