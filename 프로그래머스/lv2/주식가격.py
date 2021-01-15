def solution(prices):
    answer = len(prices)*[0]
    for k in range(len(prices)):
        for v in range(k+1,len(prices)):
            answer[k] +=1
            if prices[k]>prices[v]:
                break
    return answer