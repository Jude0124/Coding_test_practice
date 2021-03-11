def solution(n, k):
    import math
    answer,deck = [],[i for i in range(1, n+1)]
    while n:
        case = math.factorial(n-1)
        index = (k-1)//case
        k = k % case
        answer.append(deck.pop(index))
        n -= 1
    return answer