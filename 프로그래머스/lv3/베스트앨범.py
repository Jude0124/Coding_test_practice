from collections import defaultdict
def solution(g, p):
    count,index,answer = defaultdict(int),defaultdict(dict),[]
    for i in range(len(g)):
        count[g[i]] += p[i]
        index[g[i]][i] = p[i]
    for i in sorted(count.items(),key= lambda x : x[1], reverse = True):
        cnt = 0
        for j in sorted(index[i[0]].items(),key = lambda x : x[1], reverse = True):
            if cnt == 2:
                break
            cnt += 1
            answer.append(j[0])
    return answer