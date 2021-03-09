def solution(n):
    st,sp,gl,an = 1,2,3,[]
    return hanoi(st,sp,gl,an,n)

def hanoi(st,sp,gl,an,n):
    if n == 1:
        an.append([st,gl])
    else:
        hanoi(st,gl,sp,an,n-1) # A
        an.append([st,gl])     # B
        hanoi(sp,st,gl,an,n-1) # C
    return an

# 재귀 알고리즘

# D. N개의 원판에 대하여 아래 A,B,C를 순차적으로 수행한다.
# A. N-1개의 원판을 시작원판에서 보조 원판으로 옮긴다. (목표원판을 보조원판으로 이용)
# B. 가장 큰 맨밑 원판을 시작원판에서 목표 원판으로 옮긴다.
# C. N-1개의 원판을 보조원판에서 목표원판으로 옮긴다. (시작원판을 보조원판으로 이용)

# A,C단계일때, N-1개에 대하여 D 알고리즘을 재귀적으로 수행한다.


# 예시) 원판이 4개일때
# D(4) = A(3),B(3),C(3)
# A(3) = D(3) = A(2),B(2),C(2)
# A(2) = D(2) = A(1),B(1),C(1)
# C(2) = D(2) = A(1),B(1),C(1)
# C(3) = D(3) = A(2),B(2),C(2)

# D(4) = [[A(1),B(1),C(1),[B(2)],A(1),B(1),C(1)],[B(3)], [A(1),B(1),C(1),[B(2)],A(1),B(1),C(1)]]

