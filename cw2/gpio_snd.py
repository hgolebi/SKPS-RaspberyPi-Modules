import time
import gpio4
import datetime
import math

gpio = gpio4.SysfsGPIO(22)
gpio.export = True
gpio.direction = 'out'

period = 0.01
change = 0.00003

frequencies = [256, 288, 320, 341.3, 384, 432, 480, 512]

for freq in frequencies:
	period = 1/freq
	for i in range (math.floor(1/period)):
		gpio.value = 0
		time.sleep(period/2)
		gpio.value = 1
		time.sleep(period/2)
gpio.export = False
	
	
