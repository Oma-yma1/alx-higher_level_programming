#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_di = abs(number) % 10
if number < 0:
    last_di = -last_di
if last_di > 5:
    print(f"Last digit of {number} is {last_di} and is greater than 5")
elif last_di == 0:
    print(f"Last digit of {number} is {last_di} and is 0")
else:
    print(f"Last digit of {number} is {last_di} and is less than 6 and not 0")
