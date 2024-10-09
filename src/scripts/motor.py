import time

import board
import pwmio

class ServoMotor:
    ON = 2 ** 16
    MOTOR_MIN = 0.15
    MOTOR_MAX = 0.80

    def __init__(self, pin, **kwargs):
        self.motor = pwmio.PWMOut(pin, variable_frequency=False, **kwargs)
        self.motor.frequency = 330
        self.percentage = 0

    def rotate(self, n):
        """
        Rotate the servo motor by the percentage indicates by n.
            n = 0 -> 0% = 0 degrees
            n = 50 -> 50% = 90 degrees
            n = 100 -> 100% = 180 degrees
        The servo motor 
        """
        n = float(n)

        delta = ServoMotor.MOTOR_MAX - ServoMotor.MOTOR_MIN
        duty = ServoMotor.MOTOR_MIN + delta * n / 100
        self.motor.duty_cycle = duty * ServoMotor.ON
        self.percentage = n


# Initialize the motor.
motor = ServoMotor(board.D12)

while True:
    motor.rotate(0)
    time.sleep(1)
    motor.rotate(100)
    time.sleep(1)
