import re
import itertools

def solution(e):
    num_row = re.split(r"\*|\+|-",e) #1. 정규식을 이용하여 문자 기호 분리
    flag_row = re.findall(r"\D",e)  
    case = list(set(flag_row))      
    answer = []

    for i in itertools.permutations(case,len(case)): # 모든 경우의 수 조합에 대하여 돌리기
        num = num_row[:]
        flag = flag_row[:]
        for j in i:
            c = 0                                   # 완전 탐색을 위해 삭제한만큼 땡겨주기 위해 변수 설정
            for k in range(len(flag)):
                if j == flag[k-c]:
                    num[k-c+1] = str(eval(num[k-c]+flag[k-c]+num[k-c+1])) 
                    num.pop(k-c)
                    flag.pop(k-c)
                    c += 1

        answer.append(abs(int(num[0])))
    return max(answer)

# 다른사람 풀이
# 보자마자 소름이 돋았던.... 아무런 라이브러리도 사용하지 않았으며 완전탐색도 필요없다. 다른 방식의 알고리즘을 이용한 접근!!
# 모든 경우의 수에 대하여 split과 join을 이용하여 operation 기준 가장 마지막 기호 부터 
# 우선순위로 하여 괄호를 짜주는 방식으로 거꾸로 문제를 풀어냄
# 심지어 세가지 수식 기호 중 하나가 없는 테케의 경우도 기가막히게 에러를 내지 않고 무결하게 풀어낼 수 있다.

def solution2(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)