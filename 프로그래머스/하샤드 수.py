def solution(x):
    return x%sum([int(i) for i in list(str(x))]) == 0