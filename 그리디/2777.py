# 숫자 놀이 (실버2)
# https://www.acmicpc.net/problem/2777

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    result = 0
    n = int(input())
    if n < 10:
        print(1)
        continue
    div = [0] * 10

    for i in range(9, 1, -1):
        # 나누어 떨어지는 수일떄
        while n%i == 0:
            n = n//i
            div[i] += 1

    #result = sum(div)
    if n == 1:
        result = sum(div)
    else:
        result = -1
    print(result)