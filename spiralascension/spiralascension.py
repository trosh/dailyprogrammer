#!/usr/bin/env python3

import sys

try:
    n = int(sys.argv[1])
except ValueError:
    print("error: need an integer")
    sys.exit(1)
except IndexError:
    print("usage: {} <n> [ccw|cw]".format(sys.argv[0]))
    sys.exit(1)

ccw = False # counterclockwise
if len(sys.argv) == 3:
    ccw = sys.argv[2] == "ccw"

grid = []
for line in range(n+2):
    grid.append([False] * (n+2))
for i in range(n):
    for j in range(n):
        grid[i+1][j+1] = None
x = 1
y = 1
dx = 1
dy = 0
for v in range(n*n):
    grid[x][y] = v+1
    if grid[x+dx][y+dy] is not None:
        dx, dy = -dy, dx
    x += dx
    y += dy
mid = (n+1)//2
maxlen = len(str(grid[mid][mid]))
fmt = "{:<" + str(maxlen) + "}"
for i in range(1, n+1):
    for j in range(1, n+1):
        v = grid[i][j] if ccw else grid[j][i]
        print(fmt.format(v), end=" ")
    print()
