import re
def solution(s):
    answer = []
    for i in sorted(re.findall(r'\d[,\d]*',s),key = len):
        answer.extend(list(set(list(map(int,i.split(",")))) - set(answer)))
    return answer

# 정규표현식 고민하지 않고 바로 작성할 수 있을때까지 숙달하기