import smbus
import time
from constants import *

from smbus import SMBus
I2C_ID = 0x68

bus = SMBus(2)

class MPU9250:
    """Constructor"""
    def __init__(self,address=MPU_9250_I2C_SLAVE_ADDR):
        self.address=address
        self.config_mpu9250(GYRO_RANGE_250, ACCEL_RANGE_2G)
    
    def is_connected(self):
        whoami = bus.read_byte_data(self.address, WHO_AM_I)
        if (whoami == MPU_9250_I2C_DEVICE_ID):
            return True
        else:
            return False

    def config_mpu9250(self,gyro_range,accel_range):
        if gyro_range == GYRO_RANGE_250:
            self.grange = 250.0/32768.0
        elif gyro_range == GYRO_RANGE_500:
            self.grange = 500.0/32768.0
        elif gyro_range == GYRO_RANGE_1000:
            self.grange = 1000.0/32768.0
        elif gyro_range == GYRO_RANGE_2000:
            self.grange = 2000.0/32768.0
        
        if accel_range == ACCEL_RANGE_2G:
            self.arange = 2.0/32768.0
        elif accel_range == ACCEL_RANGE_4G:
            self.arange = 4.0/32768.0
        elif accel_range == ACCEL_RANGE_8G:
            self.arange = 8.0/32768.0
        elif accel_range == ACCEL_RANGE_16G:
            self.arange = 16.0/32768.0
    
        bus.write_byte_data(self.address, PWR_MGMT_1, 0x00)
        time.sleep(0.1)

        bus.write_byte_data(self.address, PWR_MGMT_1, 0x01)
        time.sleep(0.1)

        bus.write_byte_data(self.address, CONFIG, 0x03)
        bus.write_byte_data(self.address, SMPLRT_DIV, 0x04)
        bus.write_byte_data(self.address, GYRO_CONFIG, gyro_range << 3)
        bus.write_byte_data(self.address, ACCEL_CONFIG, accel_range << 3)
        bus.write_byte_data(self.address, ACCEL_CONFIG_2, 0x03)
        bus.write_byte_data(self.address, INT_PIN_CFG, 0x02)
        time.sleep(0.1)

    def data_ready(self):
        ready = bus.read_byte_data(self.address, INT_STATUS)
        if ready & 0x01:
            return True
        else:
            return False

    def read_accel(self):
        accel_data = bus.read_i2c_block_data(self.address, ACCEL_OUT, 6)
        x_accel = self.convert(accel_data[1],accel_data[0])
        y_accel = self.convert(accel_data[3],accel_data[2])
        z_accel = self.convert(accel_data[5],accel_data[4])
        
        x_accel = round(x_accel*self.arange, 3)
        y_accel = round(y_accel*self.arange, 3)
        z_accel = round(z_accel*self.arange, 3)

        return {"x":x_accel, "y":y_accel, "z":z_accel}

    def read_gyro(self):
        gyro_data = bus.read_i2c_block_data(self.address, GYRO_OUT, 6)
        x_gyro = self.convert(gyro_data[1],gyro_data[0])
        y_gyro = self.convert(gyro_data[3],gyro_data[2])
        z_gyro = self.convert(gyro_data[5],gyro_data[4])

        x_gyro = round(x_gyro*self.grange, 3)
        y_gyro = round(y_gyro*self.grange, 3)
        z_gyro = round(z_gyro*self.grange, 3)

        return {"x":x_gyro, "y":y_gyro, "z":z_gyro}

    def convert(self,lbyte,hbyte):
        value = lbyte | (hbyte << 8)
        if(value & (1 << 16 - 1)):
            value -= (1<<16)
        return value