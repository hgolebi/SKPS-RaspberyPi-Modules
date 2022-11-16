import time
import gpio4

button = gpio4.SysfsGPIO(18)
led = gpio4.SysfsGPIO(27)

button.export = True
button.direction = 'in'
led.export = True
led.direction = 'out'
while(True):
	while(button.value == 1):
		led.value = 0
	led.value = 1
button.export = False
led.export = False
