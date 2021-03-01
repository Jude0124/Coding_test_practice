def solution(t):
    for i in range(len(t)-1,-1,-1):
        for j in range(len(t[i])-1):
            if i != 0:
                t[i-1][j] += max(t[i][j],t[i][j+1])
    return t[0][0]