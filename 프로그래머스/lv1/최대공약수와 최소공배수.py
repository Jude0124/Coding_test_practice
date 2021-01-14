def solution(n, m):
    temp = 0
    answer = []
    for i in range(1,(max([n,m])//2+1)):
        if (n%i == 0) and (m%i ==0):
            temp = i
    answer.append(temp)
    answer.append(n*m/temp)
    return answer