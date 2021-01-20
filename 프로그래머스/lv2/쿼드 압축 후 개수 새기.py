def solution(arr):
    cnt0 = sum(arr,[]).count(0)
    cnt1 = sum(arr,[]).count(1)
    
    if cnt0 == len(arr)**2: return[1,0]
    
    elif cnt0 == 0: return[0,1]
    
    arr = [arr]
    
    while len(arr[0]) != 2:
        tmp = []
        for i in arr:
            x = int(len(i)/2)
            for k in [0,x]:
                for j in [0,x]:
                    a = [row[j:j+x] for row in i[k:k+x]]
                    if 1 not in sum(a,[]):
                        cnt0 -= len(a)**2-1
                    elif 0 not in sum(a,[]):
                        cnt1 -= len(a)**2-1
                    else:
                        tmp.append(a)

        arr = tmp
        if tmp == []:
            break
            
    return [cnt0,cnt1]

# 20/01/18
# 1.문제를 제대로 읽지 않아서 시간을 많이 날렸음!! 문제 똑바로 읽을 것.
# 2.코드가 바로 떠오르지 않을때는 알고리즘 순서도를 작성한 후 해당 알고리즘에 맞게 하나씩 짜보기...
# 3.함수와 클래스 다시 공부,,, 여러번 도는 loop의 경우 함수를 따로 만들어서 이쁘게 정리하는 습관 기를것!
# 4.처음엔 numpy pandas 사용하지 않고 풀어보되, 코테에서 numpy와 pandas가 사용가능하다면 적극 사용할것, numpy,pandas 추후 다시공부..

# 다른 사람 풀이 

import numpy as np

def solution2(arr):
    # 재귀함수 구현
    def fn(a):
        if np.all(a == 0): return np.array([1, 0])
        if np.all(a == 1): return np.array([0, 1])
        n = a.shape[0]//2
        return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])

    # 결과 리턴
    return fn(np.array(arr)).tolist()

