from itertools import permutations
def solution(n,w,d):    
    weak = w + [n+i for i in w]
    p = 1
    while p <= len(d):
        for i in map(list,permutations(d,p)):
            for j in range(len(w)):
                cnt,now = 1,0
                entry = i[:]
                while entry:
                    k = entry.pop()
                    while weak[j+cnt+now] - weak[j+now] <= k:
                        cnt += 1
                        if cnt+now == len(w):
                            break
                    if cnt+now == len(w):
                        return p
                    now += cnt
                    cnt = 1
        p += 1
    return -1

# 0. 수리 지점을 선형으로 변환해준다. ex) (10 -> 1) => (10 -> 13) N == 12

# permutations 을 이용한 완전 탐색
# p = 최소 탐색인원,default = 1

# 1.수리가능 인원중 p 만큼 순서에 상관 있게 entry를 추출 후,

# 2.출발 가능한 모든 좌표에 대하여 해당 entry로 모든 지점이 수리 가능한지 탐색.

# 3.entry(1명 이상)에서 한 인원씩 추출 

# 4.첫번째 인원 부터 출발점에서 자신의 수리가능 지점까지 수리한뒤, 다음인원이 미 수리 지점부터 수리 시작
# 4-1. 모든 인원이 수리 후 수리완료지점의 수가 전체 지점의 수와 일치하면 해당 인원이 최소인원이므로, return p

# 5. 모든 인원이 참여했음에도 수리가 불가능 하다면 다음 출발점에 대하여 3번부터 다시 반복 수행

# 6. 모든 출발점에 대하여 해당 entry로 수리가 불가능 하다면 다음 entry에 대하여 2 번부터 다시 반복 수행

# 7. 모든 entry에 대하여 수리가 불가능 하다면 p를 한명 늘려준 후 1번부터 다시 반복 수행

# 8. 모든 인원이 다 참여하여 어떠한 경우에도 완벽한 수리가 불가능 할 경우 return -1