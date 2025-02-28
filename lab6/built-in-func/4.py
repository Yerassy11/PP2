import time 
import math
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)
number = 25100
delay_milisec = 2123
result = delayed_sqrt(number, delay_milisec)