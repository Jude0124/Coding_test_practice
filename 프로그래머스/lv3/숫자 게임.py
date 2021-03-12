def solution(A,B):
    A,B = sorted(A,reverse = True), sorted(B,reverse = True)
    gap,cnt = 0,0
    for i in range(len(B)):
        if B[i+gap] > A[i]: cnt += 1
        else: gap -= 1
    return cnt