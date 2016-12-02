'''
set of constants for the MPU 9250 module (register map)
'''
MPU_9250_I2C_SLAVE_ADDR             = 0x68
MPU_9250_I2C_DEVICE_ID              = 0x71

'''Register addresses'''
SMPLRT_DIV          = 0x19
CONFIG              = 0x1A
GYRO_CONFIG         = 0x1B
ACCEL_CONFIG        = 0x1C
ACCEL_CONFIG_2      = 0x1D
LP_ACCEL_ODR        = 0x1E
WOM_THR             = 0x1F
FIFO_EN             = 0x23
I2C_MST_CTRL        = 0x24
I2C_MST_STATUS      = 0x36
INT_PIN_CFG         = 0x37
INT_ENABLE          = 0x38
INT_STATUS          = 0x3A
ACCEL_OUT           = 0x3B
TEMP_OUT            = 0x41
GYRO_OUT            = 0x43
USER_CTRL           = 0x6A
PWR_MGMT_1          = 0x6B
PWR_MGMT_2          = 0x6C
WHO_AM_I            = 0x75


'''Register Values for range select registers'''
GYRO_RANGE_250      = 0x00
GYRO_RANGE_500      = 0x01
GYRO_RANGE_1000     = 0x02
GYRO_RANGE_2000     = 0x03

ACCEL_RANGE_2G      = 0x00
ACCEL_RANGE_4G      = 0x01
ACCEL_RANGE_8G      = 0x02
ACCEL_RANGE_16G     = 0x03