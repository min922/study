def solution(s):
    table = {"zero":"0", "one":"1", "two":"2", "three":"3", 
             "four":"4", "five":"5", "six":"6", "seven":"7", 
             "eight":"8", "nine":"9"}
    result = ""
    alp = ""
    for i in s:
        if i.isdigit(): result += i #숫자면 result에 추가
        else: alp += i
        if alp in list(table.keys()): #문자라면 모아서 table에 있는지 확인
            result += table[alp]
            alp = ""
    return int(result)
