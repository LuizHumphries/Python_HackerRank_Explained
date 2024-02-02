#!/bin/python3
import datetime
import os

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    t1 = int((t1 - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)).total_seconds())
    t2 = int((t2 - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)).total_seconds())
    
    return str(abs(t1 - t2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
