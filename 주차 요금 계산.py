from datetime import datetime as dt
import math

def solution(fees, records):
    answer = []
    time = []

    records = [i.split(" ") for i in records]
    carnum = list(set([i[1] for i in records])) #차번호 중복 없앰
    carnum.sort() #정렬

    for num in carnum:
        tmp = []
        for rec in records:
            if num in rec:
                tmp.append(rec[0])
        if len(tmp) % 2 == 1:
            tmp.append('23:59') #안나간 차 처리
        time.append(tmp)

    for t in time:
        alltime = 0
        for i in range(len(t)//2):
            intime = dt.strptime(t[2*i], "%H:%M") #두개씩 짝지어서 
            outtime = dt.strptime(t[2*i+1], "%H:%M")
            diff = outtime - intime
            diff = int(diff.seconds/60)
            alltime += diff
        answer.append(alltime)

    answer = [fees[1] + ((math.ceil((i-fees[0])/fees[2])) * fees[3]) if i > fees[0] else fees[1] for i in answer]

    return answer
