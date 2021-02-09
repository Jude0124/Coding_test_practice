
from itertools import product
def solution(b, r, c):
    tray = []
    for i in sorted(set(sum(b,[])))[1:]:
        t = []
        for j,k in product(range(4),range(4)):
            if b[j][k] == i:
                t.append((j,k))
        tmp = [t,list(reversed(t))]
        tray.append(tmp)
        
    [sum(i,[]) for i in list(product(*tray))]
    
    # return 

# def calc(l,b,r,c):
#     while l != []:
#         x,y = l.pop(0)
#         for i in range(min(max(c,x)
        


# 백트레킹 + dfs/bfs 문제
# 시작점에 카드가 있을지라도 해당 카드부터 제거하는것이 최단경로가 아닐 수 있음.
#
# 문제 풀기전 구상해본 알고리즘 순서도
# 카드 종류, 최대 6 가지에 대하여 각각 1쌍(2좌표)씩 있으므로 제거 순서에 대한 경우의 수는 최대 2**6 가지가 존재
#
# 1.카드 제거 순서에 대하여 모든 경우의 수를 리스트로 반환
# 2.각각의 경우에 대하여 이동횟수를 산출한다.
# 2-1. 한 좌표에서 다른 좌표로 이동하는데 최대 두가지 경로 존재. 두경로중 최소 비용 경로를 선택
# 2-2. 시작좌표부터 종료좌표까지 각 좌표를 이동할때마다 경로들중 최소 비용을 가지는 경로의 이동횟수 누적
# 2-3. 이미 계산된 경로의 비용보다 더 비용이 드는 경우 중간에 해당경로는 break로 탈출(효율성 up위해)
# 3. 최소이동횟수에 Enter(카드갯수)입력 횟수를 더 해주어 return !!