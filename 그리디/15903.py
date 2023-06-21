# 카드 합체 놀이 (실버1)
# https://www.acmicpc.net/problem/15903
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
#print(card)
for i in range(M):
    card_sum = card[0] + card[1]
    card[0] = card_sum
    card[1] = card_sum
    card.sort()
print(sum(card))