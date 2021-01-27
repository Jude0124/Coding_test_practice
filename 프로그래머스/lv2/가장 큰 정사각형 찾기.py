def solution(b):
    for i in range(1,len(b)):
        for j in range(1,len(b[0])):
            if b[i][j] != 0:
                b[i][j] = min([b[i][j-1],b[i-1][j],b[i-1][j-1]])+1
                
    return max([max(i) for i in b])**2

# 깨달은점
# 이중리스트 unpacking 함부로 해서 효율성이 떨어질 수 있음
# 1000*1000개의 2중리스트 구조의 경우,
# 1, unpacking 후 min,max,sum을 할 경우 len이 1,000,000인 리스트에 대하여 한번에 최댓값 산출
# 2. loop를 돌며 min,max,sum을 해준후 unpacking 해줄경우 len이 1000인 리스트에 대하여 총 1001번의 sum 수행
# 3. 재귀적으로 비교하는 것(2번)이 brute force(1번) 보다 훨씬 빠르다
