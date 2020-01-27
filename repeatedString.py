import math
import os
import random
import re
import sys

# s, n
# aba, 10 -> aba aba aba a
# answer: 7

# increment thorugh s, n number of times and check if it is an 'a'

# Complete the repeatedString function below.
def repeatedString(s, n):
    counter = 0
    wordLength = 0
    for x in range(n):
        for i in s:
            if wordLength > n:
                break
            wordLength += 1
            if i is 'a':
                counter += 1
    print("Number of a's: ", counter)

# repeatedString("aba", 10)

def repeated_String(s, n):
    length = len(s)
    ctr_tracker = [0] * length
    first = s[0]
    if first == 'a':
        ctr_tracker[0] = 1

    for x in range(1, length):
        if s[x] == 'a':
            ctr_tracker[x] = ctr_tracker[x-1] + 1
            print("Value at", x, ": ", ctr_tracker[x])

        else:
            ctr_tracker[x] = ctr_tracker[x-1]
            print("value at", x, ": ", ctr_tracker[x])


    k = int(n/length)

    if(n%length == 0):
        remainder = 0
    else:
        remainder = ctr_tracker[n%length - 1]

    print("K: ", k)
    print("Remainder: ", remainder)
    print("ctr_tracker value: ", ctr_tracker[length-1])
    final_ctr = k * ctr_tracker[length-1] + remainder

    return print(final_ctr)

repeated_String("bbb", 10)

