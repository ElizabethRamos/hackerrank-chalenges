#!/bin/python3

import sys


time = input().strip()
hour = time[:2]
hour = int(hour)

if time[-2:] == "PM":
    if hour != 12:
        hour = hour + 12
else:
    if hour == 12:
        hour = "00"
    else:
        hour = time[:2]

newtime = str(hour)+time[2:8]

print(newtime)
