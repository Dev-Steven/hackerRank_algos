import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    end = 10000
    yes = "YES"
    no = "NO"
    count = 0
    if v1 > v2 and x1 > x2:
        print("NO")
        return no

    if v1 < v2 and x1 < x2:
        print("NO")
        return no

    for jump in range(end):
        if( (x1+v1) == (x2+v2) ):
            return yes
        x1+=v1
        x2+=v2
    return no
