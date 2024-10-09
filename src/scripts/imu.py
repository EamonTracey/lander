import logging
import time

import adafruit_bno08x
from adafruit_bno08x.i2c import BNO08X_I2C
import board

# Initialize the BNO085, enable features, and begin calibration.
i2c = board.I2C()
bno085 = BNO08X_I2C(i2c)
bno085.initialize()
bno085.enable_feature(adafruit_bno08x.BNO_REPORT_ACCELEROMETER)
bno085.enable_feature(adafruit_bno08x.BNO_REPORT_GYROSCOPE)
bno085.enable_feature(adafruit_bno08x.BNO_REPORT_MAGNETOMETER)
bno085.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)
bno085.begin_calibration()

while True:
    calibration_status = bno085.calibration_status
    acceleration = bno085.acceleration
    gyro = bno085.gyro
    magnetic = bno085.magnetic
    quaternion = bno085.quaternion

    print(f"Calibration Status: {adafruit_bno08x.REPORT_ACCURACY_STATUS[calibration_status]}")
    print(f"Acceleration (m/s**2): {acceleration[0]} {acceleration[1]} {acceleration[2]}")
    print(f"Gyro (rad/s): {gyro[0]} {gyro[1]} {gyro[2]}")
    print(f"Magnetic (uT): {magnetic[0]} {magnetic[1]} {magnetic[2]}")
    print(f"Quaternion (w x y z): {quaternion[0]} {quaternion[1]} {quaternion[2]} {quaternion[3]}")

    time.sleep(0.25)

