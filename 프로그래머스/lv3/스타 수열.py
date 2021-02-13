from collections import defaultdict

def solution(a):
    dic = defaultdict(list)
    for i in range(len(a)):
        dic[a[i]].append(i)
    k = 0
    for i in list(dic.values()):        
        cnt,c = 0,-1
        for j in i:
            if j != 0: #
                if c == j-1: 
                    cnt +=1
                    c = j+1
                elif c == j: 
                    c = j+1
                else:   
                    cnt += 1
                    c = j
            else:          
                c = j+1
                cnt += 1
        if c == len(a):
            cnt -= 1
        k = max(k,cnt)
    return k*2

# 알고리즘 순서 // 최대 리스트의 길이는 500,000 이라하였으므로 시간복잡도를 최악의 경우로 가정하고 알고리즘을 구상.
# 1. 등장하는 숫자들을 key로, 숫자들의 index(등장한 위치좌표)들을 values(list)로 하여 딕셔너리를 짠다. ex) [1,1,3,2,1,3] -> {1:[0,1,4],3:[2,5],2:[3]}
#    시간복잡도 -> O(N)
# 2. list(dic.values()) 에 대하여 loop를 돌며 가장 각각의 값들이 스타수열로 가질 수 있는 최대 길이를 계산해준다. 
#    시간복잡도는 O(N) why? 딕셔너리 values의 총 갯수가 초기 길이와 동일하기 때문!!
# 3. 각각의 key들에 대하여 루프가 끝날 때마다 기존의 최댓값(k) 와 비교하며 최댓값을 갱신해준다.
# 4. 출력한다.
## if else(조건문) 에 대한 설명은  더 이해하기 편하고 직관적이게 추후 수정 예정
# c는 떠안고 사라진 스타수열 한쌍의 뒷좌표를 의미.