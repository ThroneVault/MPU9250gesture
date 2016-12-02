import time
import sys
from mpu9250 import MPU9250

mpu9250 = MPU9250()

try:
    while True:
        accel = mpu9250.read_accel()
        print " ax = " , ( accel['x'] )
        print " ay = " , ( accel['y'] )
        print " az = " , ( accel['z'] )

        gyro = mpu9250.read_gyro()
        print " gx = " , ( gyro['x'] )
        print " gy = " , ( gyro['y'] )
        print " gz = " , ( gyro['z'] )

        time.sleep(2)

except KeyboardInterrupt:
    sys.exit()

