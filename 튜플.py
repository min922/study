def solution(s):
    tmp = s[2:-2].split("},{") #중간에 나누는 기호 다 없애기
    number = []
    for i in tmp:
        i = (i.replace(',', ' ')).split() # , 대신 공백을 넣고 그걸 기준으로 나눠서 리스트 만듦
        number.append(i)
    number.sort(key=len) #길이순 정렬
    answer = []
    for i in range(len(number)):
        if i == 0: #원소가 하나니까 바로 넣기
            answer.append(number[i][0])
        else: #차집합
            tmp = list(set(number[i]) - set(number[i - 1]))
            answer.append(tmp[0])
    answer = [int(i) for i in answer]
    return answer
