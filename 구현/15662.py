# 톱니바퀴 (2) (골드5)
# https://www.acmicpc.net/problem/15662
import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
wheel=[deque(map(int, input().strip()))for _ in range(T)]

def move(n,d):
    global cur_right, cur_left, wheel
    origin_dir=d

    for i in reversed(range(n)): # 왼쪽의 톱니바퀴
        if wheel[i][2]!=cur_left:
            cur_left=wheel[i][6]
            wheel[i].rotate(d*-1)
            d*=-1
        else:
            break
    d=origin_dir
    for i in range(n+1,T): # 오른쪽의 톱니바퀴
        if wheel[i][6]!=cur_right:
            cur_right=wheel[i][2]
            wheel[i].rotate(d*-1)
            d*=-1
        else:
            break

K=int(input())
for _ in range(K):
    start, circle =map(int, input().split())
    cur_left,cur_right=wheel[start-1][6],wheel[start-1][2]
    wheel[start-1].rotate(circle)
    move(start-1, circle)
print(sum([1 if wheel[0] else 0 for delta,wheel in enumerate(wheel)]))