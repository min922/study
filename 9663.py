# https://www.acmicpc.net/problem/9663
import sys

def queen(depth, n, board, visited):
    global result
    if depth == n: # 끝 행까지 왔을 때
        result += 1
        return
    for i in range(n):
        if visited[i] == False: # 간 적 없으면
            board[depth] = i # depth번째 행, i번째 열에 배치
            if checkqueen(depth, board): # 놓을 수 있는지 체크
                visited[i] = True # 간적 있다고 표기
                queen(depth + 1, n, board, visited) # 다음 줄로 넘어감
                visited[i] = False # 백트래킹 위해


def checkqueen(n, board):
    for i in range(n):
        if (board[n] == board[i]) or (abs(board[n] - board[i]) == n-i): # 같은 행 or 대각선 행에 있으면
            return False # 퀸 못놓음
    return True #퀸 놓을 수 있음

n = int(sys.stdin.readline().strip())
board = [0] * n  # 1차원 리스트로 적재
visited = [False] * n
result = 0
queen(0, n, board, visited)
print(result)

# Python3으로 하니 시간초과, PyPy로 하니 통과
# 원래 백트래킹은 Python으로 하면 시간이 더 오래걸린다고 함
