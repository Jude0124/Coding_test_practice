def solution(m, n, b): # 총 풀이 소요시간  1시간
    tmp =[]
    answer = 0
    while tmp != b: # 한번 이하 코드를 수행한것에 대하여 더이상 변화가 없을 경우 제거가능한 블록을 전부 제거한 것으로 판단, loop 탈출
        tmp = b[:] # 슬라이싱을 통한 얕은 복사
        tmp2 = []
        for i in range(m-1):   # 이중포문을 통해 2X2로 완전 탐색 
            for k in range(n-1):
                if len(set([b[i][k],b[i][k+1],b[i+1][k],b[i+1][k+1]])) == 1: 
                    tmp2.extend([[i,k],[i,k+1],[i+1,k],[i+1,k+1]]) # 이미 제거되어 0으로 가득찬 2x2블록에 대하여 tmp2에                            
                                                                   # extend하는 비효율성 개선 작업 추후 필요!!                    
        for i in tmp2:
            b[i[0]] = b[i[0]][:i[1]] + "0" + b[i[0]][i[1]+1:] # 2x2 완전 탐색 결과 제거가능한 블록 "0" 으로 치환
            
        tmp3 = []       
        while tmp3 != b:   # 더이상 내려올 블록이 없을 때까지 바로 윗 블록의 큐브를 받고 윗큐브는 빈블록("0")으로 치환을 반복수행
            tmp3 = b[:]
            for i in range(1,m):
                for k in range(n):
                    if b[i][k] == "0":
                        b[i] = b[i][:k]+ b[i-1][k] + b[i][k+1:]
                        b[i-1] = b[i-1][:k] + "0" + b[i-1][k+1:]

    for i in b:
        answer += i.count("0")   # 제거한 큐브 갯수 산출

    return answer   #효율성,정확성 모두 통과 , 완.