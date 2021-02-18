def n_queen(i,col):
    n = len(col)
    cnt = 0
    
    if  i == n:
        return 1
        
    for j in range(1,n+1):
        col[i] = j
        if (promising(i,col)): # 백트래킹 유망한지 판단
                cnt += n_queen(i+1,col) # 단순히 재귀를 수행하는 것이 아니라 변수에 할당해주면 전역변수를 따로 설정하지 않아도 됨.                
    return cnt
            
                
def solution(n):
    col = [0]*n
    return n_queen(0,col)


def promising(i,col):
    for k in range(i):
        if (col[i] == col[k]) or (abs(col[i]-col[k]) == i-k): 
            return False
    return True

# 깨달은점 
# 튜플로 굳이 2차원 좌표 (x,y) 를 만들지 않아도 된다.
# 리스트의 index와 value ,딕셔너리의  key : value 형식이 이미 2차원이다.

# 모든 col에는 반드시 하나만 queen 이 존재한다는 가정으로 시작하였음
# permutation을 이용하여 모든 col과 모든 row 에 대하여 가정을 시작하면, 상대적으로 깊이는 옅게 너비는 더 넓게 
# 탐색할 수 있을듯?? 추후에 해보기!!