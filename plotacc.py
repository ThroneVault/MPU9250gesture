#!/usr/bin/env python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from mpu9250 import MPU9250
import sys
import time

mpu9250 = MPU9250()

try:
    ax = []
    ay = []
    az = []
    count = 0
    print "Do gesture after 5 seconds"
    time.sleep(5)
    while True:
        accel = mpu9250.read_accel()
        gyro = mpu9250.read_gyro()
        if gyro['y'] > 100:
            print "X:",accel['x']
            print "Y:",accel['y']
            print "Z:",accel['z']
            time.sleep(2)
        
    

except KeyboardInterrupt:
    sys.exit()
