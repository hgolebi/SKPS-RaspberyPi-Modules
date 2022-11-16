import time
import gpio4
import datetime

gpio = gpio4.SysfsGPIO(27)
gpio.export = True
gpio.direction = 'out'

period = 0.01
change = 0.00003

t = datetime.datetime.now()
delta = 0
while((datetime.datetime.now() - t).seconds < 10): 
	low_time = period
	high_time = 0
	while(high_time <= period):
		gpio.value = 0
		time.sleep(low_time)
		gpio.value = 1
		time.sleep(high_time)
		low_time -= change
		high_time += change
	high_time = period
	low_time = 0
	while(low_time <= period):
		gpio.value = 0
		time.sleep(low_time)
		gpio.value = 1
		time.sleep(high_time)
		low_time += change
		high_time -= change
		low_time += 0.00001
gpio.export = False
	
	
