
# Adjusting grades for Hackerland University

# grades adjusted for multiples of 5

# 38 and below no adjustment

import sys
import math

def roundup(x):
    return int(math.ceil(x /5.0)) * 5


n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    five = roundup(grade)
    if grade < 38:
        print (grade)
    elif abs(grade - five) < 3:
        print (five)
    else:
        print (grade)