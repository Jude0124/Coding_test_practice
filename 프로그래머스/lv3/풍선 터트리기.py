def solution(a):
    cnt,n = 0,len(a)
    left, right = [0]*n,[0]*n
    left[0],right[-1] = a[0],a[-1]
    for i in range(1,n):
        
        if left[i-1]< a[i]: left[i] = left[i-1]
        else: left[i] = a[i]
        
        if right[n-i] < a[n-i-1] : right[n-i-1] = right[n-i]
        else: right[n-i-1] = a[n-i-1]
    
    for i in range(1,n-1):
        if left[i] < a[i] and right[i] < a[i]: cnt += 1
            
    return len(a) - cnt