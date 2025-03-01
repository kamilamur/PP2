import math
import time
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000.0)
    return math.sqrt(number)

number = float(input("number: "))
delay_ms = int(input("delay in milliseconds: "))
result = delayed_sqrt(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")