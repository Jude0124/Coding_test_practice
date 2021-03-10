from itertools import permutations
def solution(n, k):
    return list(permutations([i for i in range(1,n+1)],n))[k-1]