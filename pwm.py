import sys
import datetime
from time import sleep


frequency, duty_cycle, iterations = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
if duty_cycle < 0 or duty_cycle > 1:
    raise ValueError('duty_cycle has to be in range <0, 1>')

period = 1/frequency
high_time = duty_cycle * period
low_time = period - high_time
for it in range(iterations):
    print(datetime.datetime.now().time(), "low")
    sleep(low_time)
    print(datetime.datetime.now().time(), "high")
    sleep(high_time)
