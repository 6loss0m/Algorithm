# 트럭 (실버1)
# https://www.acmicpc.net/problem/13335
N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * W
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(time)

