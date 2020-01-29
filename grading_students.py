import math
import os
import random
import re
import sys

# doesnt work because

def gradingStudents(grades):
    for i, grade in enumerate(grades):
        check1 = grade + 1
        check2 = grade + 2
        if check2 < 40:
            continue
        if check1%5 == 0:
            grades[i] = check1
        elif check2%5 == 0:
            grades[i] = check2
        else:
            continue
    return grades

grades = [74, 67, 38, 33]
gradingStudents(grades)