import time
import board
import busio
import adafruit_ina260
 
i2c = board.I2C()
ina260 = adafruit_ina260.INA260(i2c)

amps = ina260.current * 0.001
volts = ina260.voltage
watts = ina260.power * 0.001

print(amps, volts, watts, end=" ")