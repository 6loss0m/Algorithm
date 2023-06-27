import sys
input = sys.stdin.readline
N, M = map(int, input().split())
move = [[-1,0],[0,1],[1,0],[0,-1]] # U, R, D, L
direct = ['U','R','D','L']
board = []
for i in range(N):
    board.append(list(input().strip()))
PR, PC = map(int, input().split())
max_index = 0
for i in range(4):
    cur_pr, cur_pc = (PR-1), (PC-1)
    dx, dy = move[i][0],move[i][1]
    cnt = 0
    while True:
        #print(cur_pr,cur_pc,dx,dy)
        cur_pr += dx
        cur_pc += dy
        cnt += 1
        #print(cur_pr,PR-1,cur_pc,PC-1,move[i][0],dx,move[i][1],dy)
        if 0 > cur_pr or cur_pr >= N or 0 > cur_pc or cur_pc >= M:
            break
        if cur_pr == (PR-1) and cur_pc == (PC-1) and move[i][0] == dx and move[i][1] == dy:
            print(direct[i])
            print("Voyager")
            exit()
        if board[cur_pr][cur_pc] == '/':
            #print("/ 접촉")
            dx, dy = dy, dx
            dx = -dx
            dy = -dy
        elif board[cur_pr][cur_pc] == '\\':
            #print("\ 접촉")
            dx, dy = dy, dx
        elif board[cur_pr][cur_pc] == 'C':
            break


    if i == 0:
        max_index = i
        max_count = cnt
    else:
        if max_count < cnt:
            max_index = i
            max_count = cnt
    #print(board)
print(direct[max_index])
print(max_count)
