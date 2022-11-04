def solution(numbers, hand):
    l_fin = 10 # *
    r_fin = 12 # #
    answer = ""
    numbers = [i if i != 0 else 11 for i in numbers] # 주어진 번호에 0이 있으면 11로 바꿈
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            l_fin = num
        elif num in [3, 6, 9]:
            answer += "R"
            r_fin = num
        else:
            l_row, l_col = divmod(l_fin, 3) #위치 계산 위해 행렬로 바꿈
            if l_col == 0: #3, 6, 9는 나머지를 3으로 만들어주기위해 
                l_col += 3
                l_row -= 1
            r_row, r_col = divmod(r_fin, 3)
            if r_col == 0:
                r_col += 3
                r_row -= 1
            n_row, n_col = divmod(num, 3)
            if n_col == 0:
                n_col += 3
                n_row -= 1
            if (abs(l_row - n_row) + abs(l_col - n_col)) > (abs(r_row - n_row) + abs(r_col - n_col)): #가로세로 거리계산
                answer += "R"
                r_fin = num
            elif (abs(l_row - n_row) + abs(l_col - n_col)) < (abs(r_row - n_row) + abs(r_col - n_col)):
                answer += "L"
                l_fin = num
            else:
                if hand == "right":
                    answer += "R"
                    r_fin = num
                else:
                    answer += "L"
                    l_fin = num
    return answer
