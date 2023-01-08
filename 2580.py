# https://www.acmicpc.net/problem/2580
import sys

def sudoku(n):
    if n == len(blank): # 끝까지 오면
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
        return # 프린트 완료하면 종료(return board 하면 None이 나옴 -> 이유 찾아보기)
    for i in range(1, 10):
        x = blank[n][0] # 빈칸의 x좌표
        y = blank[n][1] # 빈칸의 y좌표
        if checknum(x, y, i): # 숫자 넣을 수 있으면
            board[x][y] = i # 넣고
            sudoku(n + 1) # 다음
            board[x][y] = 0 # 백트래킹

def checknum(x, y, n):
    for i in range(9): # 행에 n 있는지 확인
        if n == board[x][i]:
            return False
    for i in range(9): # 열에 n 있는지 확인
        if n == board[i][y]:
            return False
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3): # 3x3에 n 있는지 확인
        for j in range(3):
            if n == board[nx+1][ny+1]:
                return False
    return True

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
blank = [[i, j] for i in range(9) for j in range(9) if board[i][j] == 0]

sudoku(0)
# 시간초과 나긴 함
