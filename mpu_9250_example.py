#!/usr/bin/env python 
import time
import sys
import thread
from mpu9250 import MPU9250
import Queue
import socket

gestureQueue = Queue.Queue(10)

mpu9250 = MPU9250()
num_samples = 10

if mpu9250.is_connected() == False:
    print "No I2C Connection!"
    sys.exit()
else:
    print "Device connected"


def detect_gesture(thread_name):
    try:
        print thread_name
        while True:
            accel = mpu9250.read_accel()
            gyro  = mpu9250.read_gyro()
            gx = 0
            gy = 0
            gz = 0
            ax = 0
            ay = 0
            az = 0
            count = 0
            while count < num_samples:
                ax = ax + accel['x']
                ay = ay + accel['y']
                az = az + accel['z']
                gx = gyro['x']
                gy = gyro['y']
                gz = gyro['z']
                count = count + 1
            ax = ax / num_samples
            ay = ay / num_samples
            az = az / num_samples
            detect = 0
            if (ax <= 0.150 and ax >= -0.020) and (ay <= 0.120 and ay >= -0.020) and (az <= 0.800):
                detect = 1
                print "Detect vertical down"
                gestureQueue.put("voldown 5")
                print " ax = " , ax
                print " ay = " , ay
                print " az = " , az
                time.sleep(2)
            
            elif (ax <= 0.150 and ax >= -0.020) and (ay <= 0.120 and ay >= -0.020) and (az >= 1.200):
                detect = 1
                print "Detect vertical up"
                #gestureQueue.put("volup")
                gestureQueue.put("volup 5")
                print " ax = " , ax
                print " ay = " , ay
                print " az = " , az
                time.sleep(2)
            
            elif (gy > 100 and ax <0):
                detect = 1
                print "Left Tilt"
                time.sleep(2)

            elif (gy > 100 and ax > 0):
                detect = 1
                print "Right Tilt"
                time.sleep(2)

            if detect:
				print "Timeout over"
				detect = 0

    except KeyboardInterrupt:
        sys.exit()

'''
gyro = mpu9250.read_gyro()
gx = 0
gy = 0
gz = 0
count = 0
while count < num_samples:
gx = gx + gyro['x']
gy = gy + gyro['y']
gz = gz + gyro['z']
count = count + 1
gx = gx / num_samples
gy = gy / num_samples
gz = gz / num_samples
print " gx = " , gx 
print " gy = " , gy 
print " gz = " , gz 
'''

def send_to_laptop(thread_name):
    TCP_IP = '192.168.0.13'
    TCP_PORT = 50000
    BUFFER_SIZE = 1024
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send("enqueue lukachupi.webm\n")
    time.sleep(0.1)
    s.send("enqueue VID_2.mp4\n")
    time.sleep(0.1)
    s.send("play\n")

    while True:
        gesture = gestureQueue.get() + "\n"
        print gesture
        s.send(gesture)

    s.close()

try:
    thread.start_new_thread(detect_gesture, ("Gesture detection thread",))
    thread.start_new_thread(send_to_laptop, ("Send to laptop thread",))

except:
    print "Thread error"

while 1:
    pass
