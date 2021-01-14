def solution(n):
    ans = set()
    for i in range(len(n)):
        for j in range(len(n)):
            if i!=j:
                ans.add(n[i]+n[j])
    answer = list(sorted(ans))
    
    return answer