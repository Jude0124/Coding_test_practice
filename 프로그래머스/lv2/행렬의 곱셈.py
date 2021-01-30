#np.dot 이 너무 마렵지만 원리를 구현해보자..
def solution(a,b):
    answer = []
    for i in range(len(a)):
        t = []
        for j in range(len(b[0])):
            c = 0
            for k in range(len(b)):
                c += a[i][k]*b[k][j]
            t.append(c)
        answer.append(t)

    return answer