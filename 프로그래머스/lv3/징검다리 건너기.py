def move(s,k,n):
    cnt = 0
    for i in range(len(s)):
        if s[i] < n:
            cnt += 1
            if cnt == k:return False
        else: cnt = 0
    return True

def solution (s,k):
    left, right = 1, max(s)+1
    while left <= right:
        mid = (left+right)//2
        if move(s,k,mid): left = mid+1
        else: right = mid-1
    return left-1


# binary search