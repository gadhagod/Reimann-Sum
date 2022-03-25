from sys import argv
from graph import makeGraph

def getTrapezoidArea(b1, b2, h):
    return h * (b1 + b2) / 2

limit, interval, exponent, y_intercept = float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4])
y_coordinates, areas, j = [], [], 0

while True:
    y_coordinates.append(j ** exponent + y_intercept)
    if(j >= limit):
        break
    j += interval

for i in range(len(y_coordinates)):
    area = getTrapezoidArea(
        0 if i == 0 else y_coordinates[i-1], 
        y_coordinates[i],
        interval
    )
    areas.append(area)

result = 0
for i in areas:
    result += i

makeGraph(y_coordinates, limit, exponent, areas, result, interval, y_intercept)