import os
import sys

def timeConversion(s):
    pm = "PM"
    a = s.split(":")
    colon = ":"

    if pm in s:
        if a[0] != "12":
            a[0] = str(int(a[0])+12)
    else:
        if a[0] == "12":
            a[0] = "00"

    militaryTime = colon.join(a)
    print(str(militaryTime[:-2]))
    return str(militaryTime[:-2])

s = "12:05:45PM"
timeConversion(s)