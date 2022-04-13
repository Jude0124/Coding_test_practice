from itertools import product,permutations
from copy import deepcopy

def solution(b, r, c):
    tray = []
    for i in sorted(set(sum(b,[])))[1:]:
        t = []
        for j,k in product(range(4),range(4)):
            if b[j][k] == i:
                t.append((j,k))
                b[j][k] = 1
        tmp = [t,list(reversed(t))]
        tray.append(tmp)
    a,b_raw = [],b
    for i in list(product(*tray)):
        for j in permutations(i):
            b = deepcopy(b_raw)
            a.append(calc(sum(j,[]),b,r,c))
            
    return min(a)

def calc(l,b,r,c):
    cnt = 0
    while l != []:
        x,y = l.pop(0)
        cnt1 = abs(x-r)+abs(y-c)
        cnt2 = cnt1
        s1,s2 = "",""
        if x != r:
            r2 = int((x-r)/abs(x-r))
            for i in range(r+r2,x+r2,r2):
                s1 += str(b[i][c])
                s2 += str(b[i][y])
            if (s1 in ["01","101","011"]) or ((x == 3 or x == 0) and s1 == "00"):
                cnt1 -= 1
            elif s1 in ["001","000"]:
                cnt1 -= 2
            if (s2 in ["01","101","011"]) or ((x == 3 or x == 0) and s2 == "00"):
                cnt2 -= 1
            elif s2 in ["001","000"]:
                cnt2 -= 2
            
        s1,s2 = "","" 
        if y != c:
            c2 = int((y-c)/abs(y-c))
            for j in range(c+c2,y+c2,c2):
                s1 += str(b[x][j])
                s2 += str(b[r][j])
            if (s1 in ["01","101","011"]) or ((y == 3 or y == 0) and s1 == "00"):
                cnt1 -= 1
            elif s1 in ["001","000"]:
                cnt1 -= 2
            if (s2 in ["01","101","011"]) or ((y == 3 or y == 0) and s2 == "00"):
                cnt2 -= 1
            elif s2 in ["001","000"]:
                cnt2 -= 2
        cnt += min(cnt1,cnt2)+1     
        r,c = x,y
        b[r][c] = 0
    return cnt

# 백트레킹 + dfs/bfs 문제 풀이 소요시간 3시간+a
# 시작점에 카드가 있을지라도 해당 카드부터 제거하는것이 최단경로가 아닐 수 있음.
#
# 문제 풀기전 구상해본 알고리즘 순서도
# 카드 종류, 최대 6 가지에 대하여 각각 1쌍(2좌표)씩 있으므로 제거 순서에 대한 경우의 수는 최대 (2**6)*6! (46080) 가지가 존재

# 1.카드 제거 순서에 대하여 모든 경우의 수를 리스트로 반환
# 2.각각의 경우에 대하여 이동횟수를 산출한다.
# 2-1. 한 좌표에서 다른 좌표로 이동하는데 최대 두가지 경로 존재. 두경로중 최소 비용 경로를 선택
# 2-2. 시작좌표부터 종료좌표까지 각 좌표를 이동할때마다 경로들중 최소 비용을 가지는 경로의 이동횟수 누적
# 2-3. 이미 계산된 경로의 비용보다 더 비용이 드는 경우 중간에 해당경로는 break로 탈출(효율성 up위해)
# 3. 최소이동횟수에 Enter(카드갯수)입력 횟수를 더 해주어 return !!
# 
#210211_ 2칸 이동의 경우 목표점의 index가 이동횟수에 영향을 미치는 경우가 있어서 애먹었다.. 
# 같은 빈칸 두칸을 이동할지라도 마지막칸이 벽에 인접한다면 ctrl 이동으로 한번이지만
# 마지막칸이 벽에 인접하지 않다면 두번이동하므로 두칸이동의 경우 목표좌표의 index 또한 경로 이동거리에 영향을 미친다