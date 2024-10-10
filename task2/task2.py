import math as m
import sys

file_circle = sys.argv[1]
file_points = sys.argv[2]

with open(file_circle, 'r') as file:
    line1 = file.readline().strip().split()
    x0 = int(line1[0])
    y0 = int(line1[1])

    r = int(file.readline().strip())

with open(file_points, 'r') as file:
    for line in file:
        x1, y1 = map(int, line.strip().split())

        d = m.sqrt((x1-x0)**2+(y1-y0)**2)
        if d > r:
            print(2)
        elif d == r:
            print(0)
        else:
            print(1)

