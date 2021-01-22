import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s[:2])
    if s[-2] == "P":
        hour+=12 if hour != 12 else 0
    else:
        if hour == 12: hour = 0
    return f"{str(hour).zfill(2)}{s[2:-2]}"

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
