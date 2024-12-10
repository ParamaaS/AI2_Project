from cmath import inf
from collections import deque
from typing import List


def findShortestWay(maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    m, n = len(maze), len(maze[0])
    r, c = ball
    rh, ch = hole
    q = deque([(r, c)])
    dist = [[inf] * n for _ in range(m)]
    dist[r][c] = 0
    path = [[None] * n for _ in range(m)]
    path[r][c] = ''
    while q:
        i, j = q.popleft()
        for a, b, d in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
            x, y, step = i, j, dist[i][j]
            while (
                0 <= x + a < m
                and 0 <= y + b < n
                and maze[x + a][y + b] == 0
                and (x != rh or y != ch)
            ):
                x, y = x + a, y + b
                step += 1
            if dist[x][y] > step or (
                dist[x][y] == step and path[i][j] + d < path[x][y]
            ):
                dist[x][y] = step
                path[x][y] = path[i][j] + d
                if x != rh or y != ch:
                    q.append((x, y))
    return path[rh][ch] or 'impossible'

def takeAction(maze: List[List[int]], ball: List[int], action: str):
    if (action == 'u'):
        move = (-1, 0)
    elif (action == 'd'):
        move = (1, 0)
    elif (action == 'l'):
        move = (0, -1)
    elif (action == 'r'):
        move = (0, 1)
    while (
        0 <= ball[0] < len(maze) and
        0 <= ball[1] < len(maze[0]) and
        0 <= ball[0] + move[0] < len(maze) and
        0 <= ball[1] + move[1] < len(maze[0]) and
        maze[ball[0] + move[0]][ball[1] + move[1]] == 0
    ):
        ball[0] += move[0]
        ball[1] += move[1]
    return ball       

def printMaze(maze: List[List[int]], ball: List[int], hole: List[int]):
    for i in range(len(maze[0]) + 2):
        print("1", end = " ")
    print()
    for i in range(len(maze)):
        print("1", end = " ")
        for j in range(len(maze[i])):
            if (i == ball[0] and j == ball[1]):
                print("B", end = " ")
            elif (i == hole[0] and j == hole[1]):
                print("H", end = " ")
            else:
                print(str(maze[i][j]), end = " ")
        print("1", end = " ")
        print()
    for i in range(len(maze[0]) + 2):
        print("1", end = " ")
    print()
    print("-" * (len(maze[0]) * 2 + 3))