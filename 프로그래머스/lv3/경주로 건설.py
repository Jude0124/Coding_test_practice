# 알고리즘 순서도
# 1. 현재 좌표 0.0 기준으로 좌표가 음수값이 되지 않는다면 단위시간동안 상하좌우 1칸 이동한다.
# 1-1. 이때 이동하고자 하는곳의 좌표값이 1이거나 입력받은 죄표리스트내에 이동했던기록이 있다면
#      해당 좌표로는 이동하지 않는다.
# 2. 이전 좌표들 + 현재좌표를 리스트로 리턴
# 3. 1~2과정을 반복적으로 수행하여 (n-1,n-1) 도달할수 있는경로들의 좌표리스트들을 받아낸다.
# 4. 이중리스트내에 있는 경로들에 대하여 건설비용을 계산해주고 이중 최솟값을 리턴한다.
def move(n,k,b):
    tmp = []
    c = 0
    for i in n[:-1]:
        if i[-1] == (k-1,k-1):
            p = 2
            for u in range(1,len(i)-1):
                if abs(i[u-1][0] - i[u+1][0]) == 1:
                    p += 5
                else:
                    p += 1
            if p < n[-1]:
                n.pop()
                n.append(p)
        else:
            c += 1
            x,y = i[-1]
            for m in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if -1 in m or k in m:
                    continue
                elif b[m[0]][m[1]] == 1:
                    continue
                elif m in i:
                    continue
                else: 
                    tmp.append(i+[m])
    tmp.append(n[-1])
    if c == 0:
        return tmp
    return move(tmp,k,b)
    
def solution(b):
    k = len(b)
    s = [[(0,0)],450000]
    return move(s,k,b)
    
#     for i in range(20):
#         s = move(s,k,b)