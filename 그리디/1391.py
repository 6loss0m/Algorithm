# 회의실 배정 [실버1]
# https://www.acmicpc.net/problem/1931

N = int(input())
rooms = []
answer = []
for i in range(N):
    rooms.append(list(map(int, input().split())))
rooms.sort(key=lambda room : (room[1], room[0]))
for i in range(N):
    if i == 0:
        start, end = rooms[i]
        answer.append(rooms[i])
        continue
    if rooms[i][0] >= end:
        start, end = rooms[i]
        answer.append(rooms[i])
print(len(answer))