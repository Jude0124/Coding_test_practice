def solution(p):
    for i in range(len(p)):
        for j in p[:i]+p[i+1:]:
            if p[i] == j[:len(p[i])]: return False
    return True