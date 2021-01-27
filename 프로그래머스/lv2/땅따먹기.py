def solution(l):
    for i in range(1,len(l)):
        for j in range(4):
            l[i][j] += max(l[0][0:i]+l[0][i+1:])
    return max(l[i])

# 처음에 아래와 같이 재귀로 풀어보았으나 pop을 하는과정이 메모리 할당을 많이 먹는건지... 런타임에러가 떴음...
# 재귀로 푸는게 더 풀이과정이 직관적으로 보일 수 있으나 성능은 보장 못할 수 도 있음...;;;

def recursive(l):
    def c(n):
        if len(n) == 1: return max(n[0])
        for i in range(4):
            n[1][i] += max(n[0][0:i]+n[0][i+1:])
        n.pop(0)
        return c(n)
    return c(l)

